# Generated by Django 3.2.23 on 2024-02-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20240205_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
    ]
