# Generated by Django 4.1.3 on 2023-01-20 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_rename_image_gallery_other_image_imag3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery_other_image',
            old_name='imag3',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='gallery_other_image',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='gallery_other_image',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='gallery_other_image',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='gallery_other_image',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='gallery_other_image',
            name='image6',
        ),
    ]
