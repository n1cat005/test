# Generated by Django 5.2 on 2025-05-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_cart_basket_rename_cartitem_basketitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='price',
        ),
    ]
