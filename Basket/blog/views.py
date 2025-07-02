from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from unicodedata import category
from rest_framework.permissions import IsAdminUser
from .models import Product, Basket, BasketItem, Category, EmailVerificationCode
from .serializers import BasketSerializer, ProductSerializer, CategorySerializer, ProductFilterSerializer
from django.shortcuts import get_object_or_404
import django_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from .utils import send_verification_email


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']


class ProductFilterView(APIView):
    def get(self, request):
        products = Product.objects.all()

        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)

        in_stock = request.GET.get('in_stock')
        if in_stock is not None:
            if in_stock.lower() == 'true':
                products = products.filter(in_stock=True)
            elif in_stock.lower() == 'false':
                products = products.filter(in_stock=False)


        categories = request.GET.get('categories')
        if categories:
            category_ids = categories.split(',')
            products = products.filter(category__id__in=category_ids)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CategoryListView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)



class CategoryDetailView(APIView):

    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        category = get_object_or_404(Category, pk=pk)

        return category

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)

        return Response(serializer.data)



class CategoryView(APIView):

    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        category = get_object_or_404(Category, pk=pk)

        return category

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductView(APIView):

    def get_object(self, pk):
        product = get_object_or_404(Product, pk=pk)

        return product

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer =ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class AddToBasketView(APIView):
    def post(self, request, pk):
        user = request.user
        pk = request.data.get('pk')
        quantity = int(request.data.get('quantity', 1))

        product = get_object_or_404(Product, pk=pk)

        basket, created = Basket.objects.get_or_create(user=user)

        basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
        if not created:
            basket_item.quantity += quantity
        else:
            basket_item.quantity = quantity
        basket_item.save()

        return Response({'message': 'Mehsul sebete elave edildi'}, status=status.HTTP_200_OK)



class ViewBasketView(APIView):
    def get(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        serializer = BasketSerializer(basket)

        return Response(serializer.data)



class UpdateBasketItemView(APIView):
    def put(self, request, pk):
        user = request.user
        quantity = int(request.data.get('quantity', 1))

        basket = get_object_or_404(Basket, user=user)
        basket_item = get_object_or_404(BasketItem, basket=basket, pk=pk)

        if quantity <= 0:
            basket_item.delete()
            return Response({'message': 'Məhsul sepetdən silindi'}, status=status.HTTP_200_OK)

        basket_item.quantity = quantity
        basket_item.save()
        return Response({'message': 'Məhsulun miqdarı yeniləndi'}, status=status.HTTP_200_OK)



class RemoveFromBasketView(APIView):
    def delete(self, request, pk):
        user = request.user
        basket = get_object_or_404(Basket, user=user)
        basket_item = get_object_or_404(BasketItem, basket=basket, pk=pk)
        basket_item.delete()
        return Response({'message': 'Məhsul sepetdən silindi'}, status=status.HTTP_200_OK)



class SendVerificationCodeView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

        send_verification_email(email)
        return Response({'message': 'Doğrulama kodu emailə göndərildi.'})


class VerifyEmailCodeView(APIView):
    def post(self, request):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            record = EmailVerificationCode.objects.get(email=email)
            if record.is_expired():
                return Response({'error': 'Kodun müddəti bitib.'}, status=status.HTTP_400_BAD_REQUEST)
            if record.code == code:
                return Response({'message': 'Kod doğrudur.'})
            else:
                return Response({'error': 'Kod yanlışdır.'}, status=status.HTTP_400_BAD_REQUEST)
        except EmailVerificationCode.DoesNotExist:
            return Response({'error': 'Kod tapılmadı.'}, status=status.HTTP_404_NOT_FOUND)













































