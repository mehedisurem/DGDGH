# Generated by Django 4.1.5 on 2023-01-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_product_name_product_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_Name',
            field=models.CharField(max_length=270),
        ),
    ]