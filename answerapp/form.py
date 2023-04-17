
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from argparse import RawTextHelpFormatter
from django.core.management.base import BaseCommand
from django.db import transaction
# from typing_extensions import Required

class SignupForm(UserCreationForm):
    
    password1=forms.CharField(max_length=25,required=True,help_text='Your password can’t be too similar to your other personal information.  Your password must contain at least 8 characters.Your password can’t be a commonly used password.  Your password can’t be entirely numeric.',widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))

    password2=forms.CharField(max_length=25,help_text="Enter the same password as before, for verification.",widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password"
    }))
    email=forms.EmailField(required=True,help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={
        'placeholder':'Email'
    }))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={
        "placeholder":"First Name"
    }))
    last_name  = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={
        "placeholder":"Last Name"
    }))

   
   
  
    class Meta:
        model=User
        fields = UserCreationForm.Meta.fields + ('username','email','password1','password2','first_name','last_name')
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Username'}),
         
            
        }
    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False) 
       
        if commit:
            user.save()
        return user


