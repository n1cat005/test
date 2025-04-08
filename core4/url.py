from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact,  name='contact'),
    path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
    path('single/', views.single, name='single'),
    path('register/', views.register, name='register'),
]
