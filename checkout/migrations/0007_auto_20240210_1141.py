# Generated by Django 3.2.23 on 2024-02-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_discount_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='discount_type',
            field=models.CharField(choices=[('percentage', 'Percentage')], max_length=10),
        ),
    ]
