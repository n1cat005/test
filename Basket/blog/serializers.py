from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Product, Basket, BasketItem, Category
from django.contrib.auth.models import User

class ProductFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ['product', 'quantity', 'total_price']


class BasketSerializer(serializers.ModelSerializer):
    item = BasketItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['item', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()
















