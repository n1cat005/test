from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default=None, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uptaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket,related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price*self.quantity


class EmailVerificationCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

























