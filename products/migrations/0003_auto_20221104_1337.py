# Generated by Django 3.2.16 on 2022-11-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221104_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='products.ColorVariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='products.SizeVariant'),
        ),
    ]