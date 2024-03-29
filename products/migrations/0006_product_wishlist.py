# Generated by Django 3.2.23 on 2024-02-02 22:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_product_new_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist_item', to=settings.AUTH_USER_MODEL),
        ),
    ]
