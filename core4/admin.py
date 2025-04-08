from django.contrib import admin
from .models import (
    AboutUs,Blog,Contact,Price,Register
)
class post_filter(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class blog_filter(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class price_filter(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class Contact_filter(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'updated_at')

class Register_filter(admin.ModelAdmin):
    list_display = ('full_name', 'password', 'email', 'confirm_password', 'created_at', 'updated_at')

admin.site.register(AboutUs,post_filter)
admin.site.register(Blog,blog_filter)
admin.site.register(Contact,Contact_filter)
admin.site.register(Price,price_filter)
admin.site.register(Register,Register_filter)



