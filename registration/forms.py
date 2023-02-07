from django import forms
from django.forms import ModelForm
from . models import *

class order_form(forms.Form):
    email = forms.EmailField(
    label = '',
    error_messages = {
    'required':"please fill the email field!",
    'invalid':'you have entered an invalid email!'
    },
     widget= forms.TextInput(
        attrs={
               'class':'shadow form-control',
               'id':'user-password',
               'name':'fname',
             'placeholder':'Email'    
        }
    )
    )
    phone = forms.IntegerField(
    label="",
    error_messages = {
    'required':"please fill the phone input!",
    'invalid':'Enter a valid phone number!'
    },
     widget= forms.TextInput(
        attrs={
               'class':'shadow form-control',
               'id':'user-password',
               'name':'fname',
             'placeholder':'phone ie. +255764240465'    
        }
    )
    )
    title = forms.CharField(
        label = '',
        widget= forms.TextInput(
            attrs={
                'class':'shadow form-control',
                'id':'user-password',
                'placeholder':'name of the product you want',
                
            }
        )
    )
    description = forms.CharField(
        label = '',
        widget= forms.TextInput(
            attrs={
                'class':'shadow form-control',
                'id':'user-password',
                'placeholder':'explain about what actually you want',
                
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()





class contact_form(forms.Form):

    phone = forms.IntegerField(
    label="",
    error_messages = {
    'required':"please fill the phone input!",
    'invalid':'Enter a valid phone number!'
    },
    widget= forms.TextInput(
        attrs={
               'class':'shadow form-control',
               'id':'user-password',
               'name':'fname',
             'placeholder':'phone: ie. +255764240465'    
        }
    )
    )
    email = forms.EmailField(
    label = '',
    error_messages = {
    'required':"please fill the email field!",
    'invalid':'you have entered an invalid email!'
    },
     widget= forms.TextInput(
        attrs={
               'class':'shadow form-control',
               'id':'user-password',
               'name':'fname',
             'placeholder':'Email: ie. name@example.com'    
        }
    )
    )
    message = forms.CharField(
        label = '',
        widget= forms.TextInput(
            attrs={
                'class':'shadow form-control',
                'id':'user-password',
                'placeholder':'Message',
                
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()

class subscribe_form(forms.Form):
    email = forms.EmailField(
        label = '',
        error_messages = {
            'required':'please fill the email field!',
            'invalid':'you have entered an invalid email!'
        },
        widget = forms.TextInput(
            attrs = {
                'class': 'shadow form-control',
                'id': 'user-email',
                'placeholder':'email'
            }
        )
    )
    def clean(self):
        cleaned_data = super().clean()

