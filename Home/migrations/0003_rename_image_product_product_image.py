# Generated by Django 5.0.6 on 2024-06-09 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_product_image_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='product_image',
        ),
    ]
