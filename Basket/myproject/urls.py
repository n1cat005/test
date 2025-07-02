"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import AddToBasketView, ViewBasketView, CategoryView, VerifyEmailCodeView,SendVerificationCodeView
from blog.views import UpdateBasketItemView, RemoveFromBasketView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('user.urls')),
    path('basket/add/', AddToBasketView.as_view(), name='add_to_cart'),
    path('basket/', ViewBasketView.as_view(), name='view_cart'),
    path('basket/update/<int:product_id>/', UpdateBasketItemView.as_view(), name='update_cart_item'),
    path('basket/remove/<int:product_id>/', RemoveFromBasketView.as_view(), name='remove_cart_item'),
    path('api/', include('blog.urls')),

]

