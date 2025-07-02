from django.contrib import admin
from .models import Product, Category, Basket, BasketItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(BasketItem)


