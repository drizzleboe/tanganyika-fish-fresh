# Generated by Django 4.1.3 on 2022-12-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_other_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/')),
                ('desc', models.CharField(max_length=280, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='gallery_top_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='uploads/image-icon.jpg', upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
