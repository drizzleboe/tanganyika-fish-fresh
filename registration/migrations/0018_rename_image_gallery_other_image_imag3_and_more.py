# Generated by Django 4.1.3 on 2023-01-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_rename_imag3_gallery_other_image_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery_other_image',
            old_name='image',
            new_name='imag3',
        ),
        migrations.AddField(
            model_name='gallery_other_image',
            name='image1',
            field=models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='gallery_other_image',
            name='image2',
            field=models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='gallery_other_image',
            name='image4',
            field=models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='gallery_other_image',
            name='image5',
            field=models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='gallery_other_image',
            name='image6',
            field=models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]