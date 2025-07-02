from django.contrib import admin
from django.urls import path
from .views import CategoryView, ProductView, CategoryDetailView, CategoryListView, ProductFilterView, UpdateBasketItemView, RemoveFromBasketView, AddToBasketView, SendVerificationCodeView, VerifyEmailCodeView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('category-list/', CategoryListView.as_view()),
    path('products/<int:pk>/', ProductView.as_view()),
    path('products/', ProductView.as_view()),
    path('product-filter/', ProductFilterView.as_view()),
    path('update-basket/<int:pk>/', UpdateBasketItemView.as_view()),
    path('delete-basket/<int:pk>/', RemoveFromBasketView.as_view()),
    path('add-basket/<int:pk>/', AddToBasketView.as_view()),
    path('send-code/', SendVerificationCodeView.as_view(), name='send-code'),
    path('verify-code/', VerifyEmailCodeView.as_view(), name='verify-code'),
]

