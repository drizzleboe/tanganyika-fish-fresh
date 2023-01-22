from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import order_form,contact_form,subscribe_form
from .models import contact as db_contact, gallery_bottom,gallery_other_image,subscribers_email,our_potential,gallery_top_image, about_u, comment as cmt, product as prdct
from django.contrib import messages
from django.forms import ValidationError


import datetime


now = datetime.datetime.now()
current_year = now.year

MAX_IMAGE = 3
def has_add_permission(self, request):
    if self.gallery_top_image.objects.count() >= MAX_IMAGE:
        return False
    return super().has_add_permission(request)


# Create your views here.
def index(request):
    products = prdct.objects.all()
    about_us = about_u.objects.all()
    contact_form_1 = contact_form()
    subscribe_form_1 = subscribe_form()
    potentials = our_potential.objects.all()
    usr_comments = cmt.objects.all()
    subscribers_email_ = subscribers_email.objects.all()
    contacted = 0
    subscribed = 0
    if request.method == 'POST':
        if 'index-send-button' in request.POST:
            contact_form_1 = contact_form(request.POST or None)
            if contact_form_1.is_valid():
                phone = contact_form_1.cleaned_data.get('phone')
                email = contact_form_1.cleaned_data.get('email')
                message = contact_form_1.cleaned_data.get('message')
                new_meesage = db_contact.objects.create(
                    phone = phone,
                    email = email,
                    message = message,
                )
                if new_meesage:
                    contacted = 1
                    messages.success(request,f'Thanks for contacting us, we will get back to you soon!')
                    return HttpResponseRedirect(reverse('index') + '#alert-success')
            else:
                return HttpResponseRedirect(reverse('index') + '#alert-success')
        if 'sub_button' in request.POST:
            subscribe_form_1 = subscribe_form(request.POST or None)
            if subscribe_form_1.is_valid():
                email = subscribe_form_1.cleaned_data.get('email')
                _success = subscribers_email.objects.create(
                    email = email
                )
                if _success:
                    subscribed = True
                    messages.success(request, 'Thanks for subscription!')
                    return HttpResponseRedirect(reverse('index') + '#sub-id-section')

    return render(request, 'registration/index.html',{
        'contact_form': contact_form_1,
        'subscribe_form':subscribe_form_1,
        'potentials':potentials,
        'about_us':about_us,
        'comments':usr_comments,
        'current_year':current_year,
        'products':products,
        'contacted': contacted,
    })


def products(request):
    about_us = about_u.objects.all()
    products = prdct.objects.all()
    

   # product_size = len(products)
   # for i in range(product_size):
   #     odd = i % 2
   #     if odd:
   #         print(i
   #          )

       
 
        
    return render(request, 'registration/products.html',{
        'about_us':about_us,
        'products':products,
        'current_year':current_year,
    })


def about(request):
    products = prdct.objects.all()
    about_us = about_u.objects.all()
    return render(request, 'registration/about_us.html',{
        'about_us':about_us,
        'current_year':current_year,
        'products':products,
    })

def contact(request):
    products = prdct.objects.all()
    about_us = about_u.objects.all()
    contact_form_1 = contact_form()
    if request.method == 'POST':
        contact_form_1 = contact_form(request.POST or None)
        if contact_form_1.is_valid():
            phone = contact_form_1.cleaned_data.get('phone')
            email = contact_form_1.cleaned_data.get('email')
            message = contact_form_1.cleaned_data.get('message')
            new_meesage = db_contact.objects.create(
                phone = phone,
                email = email,
                message = message,
            )
            if new_meesage:
                messages.success(request,f'Thanks for contacting us, we will get back to you soon!')
                return redirect('contact_page')
            if not new_meesage:
                messages.warning(request, 'something went wrong, the form not yet submitted!')
                return redirect('contact_page')

    return render(request, 'registration/contacts.html',{
        'contact_form': contact_form_1,
        'about_us':about_us,
        'current_year':current_year,
        'products':products,
    })

def order(request):
    products = prdct.objects.all()
    about_us = about_u.objects.all()
    contact_form_1 = contact_form()
    if request.method == 'POST':
        contact_form_1 = contact_form(request.POST or None)
        if contact_form_1.is_valid():
            phone = contact_form_1.cleaned_data.get('phone')
            email = contact_form_1.cleaned_data.get('email')
            message = contact_form_1.cleaned_data.get('message')
            new_meesage = db_contact.objects.create(
                phone = phone,
                email = email,
                message = message,
            )
            if new_meesage:
                messages.success(request,f'Thanks for contacting us, we will get back to you soon!')
                return redirect('contact_page')
            if not new_meesage:
                messages.warning(request, 'something went wrong, the form not yet submitted!')
                return redirect('contact_page')

    return render(request, 'registration/order.html',{
        'contact_form': contact_form_1,
        'about_us':about_us,
        'current_year':current_year,
        'products':products,
    })
def gallery(request):
    products = prdct.objects.all()
    img = gallery_top_image.objects.all()[0:3]
    img2 = gallery_other_image.objects.all()
    about_us = about_u.objects.all()
    bottom_ = gallery_bottom.objects.all()
    return render(request, 'registration/gallery.html',{
        'about_us':about_us,
        'current_year':current_year,
        'top_images': img,
        'other_images': img2,
        'bottom':bottom_,
        'products':products,
    })