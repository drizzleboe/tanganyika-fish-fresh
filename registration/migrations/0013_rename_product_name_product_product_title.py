# Generated by Django 4.1.3 on 2023-01-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='product_title',
        ),
    ]
