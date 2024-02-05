# Generated by Django 3.2.23 on 2024-02-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GiftAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_answer', models.CharField(max_length=255)),
                ('associated_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.giftquestion')),
            ],
        ),
    ]
