# from typing_extensions import Required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from argparse import RawTextHelpFormatter
from django.core.management.base import BaseCommand
# from typing_extensions import Required

class SignupForm(UserCreationForm):
    
    password1=forms.CharField(max_length=25,help_text='Your password can’t be too similar to your other personal information.  Your password must contain at least 8 characters.Your password can’t be a commonly used password.  Your password can’t be entirely numeric.',widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))
    name=forms.CharField(max_length=25,help_text='Only alphabet',widget=forms.PasswordInput(attrs={
        "placeholder":"Name"
    }))
    Rollno=forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={
        "placeholder":"roll no"
    }))
    password2=forms.CharField(max_length=25,help_text="Enter the same password as before, for verification.",widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password"
    }))
    email=forms.EmailField(help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={
        'placeholder':'Email'
    }))
   
   
  
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
         
            
        }

