# Generated by Django 5.0 on 2023-12-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
