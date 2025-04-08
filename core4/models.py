from django.db import models
from django.utils.decorators import method_decorator


class AboutUs(models.Model):
    title =models.CharField(max_length=50)
    content = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)



class Contact(models.Model):
    full_name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(max_length=35, blank=True,null=True)
    subject = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Price(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)



class Register(models.Model):
    full_name = models.CharField(max_length=30,blank=True,null=True)
    password = models.CharField(max_length=35, blank=True,null=True)
    confirm_password = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)













