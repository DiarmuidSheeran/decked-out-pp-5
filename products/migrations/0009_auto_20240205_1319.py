# Generated by Django 3.2.23 on 2024-02-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_giftanswer_giftquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftanswer',
            name='associated_category',
        ),
        migrations.AddField(
            model_name='giftanswer',
            name='associated_categories',
            field=models.ManyToManyField(blank=True, to='products.Category'),
        ),
    ]
