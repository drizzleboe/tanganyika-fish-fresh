from django.db import models

# Create your models here.

class gallery_top_image(models.Model):
    image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    #desc       = models.CharField(max_length=280, null=True)    
    date        = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f'{self.image}'

    class Meta:
        verbose_name_plural = "Top images in gallery"


class gallery_other_image(models.Model):
    image1       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    image2      = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    image3       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    image4       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    image5       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    image6       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    desc        = models.CharField(max_length=280, null=True)
    date        = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.desc}'
    class Meta:
        verbose_name_plural = "Other images in gallery"

class order(models.Model):
    s_title = models.CharField(max_length = 30)
    desc = models.TextField(max_length=200, null= True, blank= True)
    #usernames = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    date        = models.DateField(auto_now=True)
    time        = models.TimeField(auto_now=True)

    def __str__(self):
        return f'{self.s_title}: placed on {self.date} {self.time}'

class contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=5000)
    date        = models.DateField(auto_now=True)
    time        = models.TimeField(auto_now=True)

    def __str__(self):
        return f'message from {self.email} received on:{self.date} {self.time}'

class our_potential(models.Model):
    heading = models.CharField(max_length= 50)
    text = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.heading}'
    class Meta:
        verbose_name_plural = "Our potentials"

class about_u(models.Model):
    heading = models.CharField(max_length= 500)
    text = models.CharField(max_length=40000)

    def __str__(self):
        return f'{self.heading}'
    class Meta:
        verbose_name_plural = "About us"
class comment(models.Model):
    #heading = models.CharField(max_length= 500)
    comment_of_the_user  = models.TextField(max_length=40000)
    image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    name_of_the_user = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.comment_of_the_user}'

class product(models.Model):
    product_title = models.CharField(max_length= 500)
    slug = models.SlugField(unique=True)
    product_description  = models.TextField(max_length=40000)
    image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    date        = models.DateField(auto_now=True)
    time        = models.TimeField(auto_now=True)


    def __str__(self):
        return f'{self.product_title}'

class subscribers_email(models.Model):
    email = models.EmailField(null=True, blank=True)
    date        = models.DateField(auto_now=True)
    time        = models.TimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.email} on {self.date}: {self.time}'

class gallery_bottom(models.Model):
    heading = models.CharField(max_length= 500)
    description  = models.TextField(max_length=40000)
    #image       = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, default="uploads/image-icon.jpg")
    #name_of_the_user = models.CharField(max_length=100)
    def __str__(self):
        return f'Description bellow the gallery page'
    
    class Meta:
        verbose_name_plural = "gallery buttom"