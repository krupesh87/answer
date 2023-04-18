from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .form import SignupForm
from .models import *
import math
from difflib import SequenceMatcher
# Create your views here.
import pytesseract
def Logout(request):
    logout(request)
    return redirect("/")

from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def Home(request):
    if request.user.is_authenticated:
        subj=QuestionandAnswer.objects.all()
        print(subj)
        return render(request,'home.html',{'subj':subj})
    # dataw=StudentResult.objects.filter(username=request.user)

    
   
    # elif(dataw):
    #     return render(request,'home.html',{'dataw':dataw[0]})   
       
        
          
            
          
       
    

    return redirect('login')
@login_required(login_url='/')
def Question(request):
    if request.user.is_authenticated: 
        subject=request.POST.get('subjects')
     
        data=QuestionandAnswer.objects.get(subject=subject)

        text1 = ""
        text2 = ""
        text3 = ""
        text4 = ""
        text5 = ""
        text6 = ""
        text7 = ""
        text8 = ""
        text9 = ""
        text10 = ""
        marks = ""
        result1 = ""
        result2 = ""
        result3 = ""
        result4 = ""
        result5 = ""
        result6 = ""
        result7 = ""
        result8 = ""
        result9 = ""
        result10 = ""
      
     
        
        
        return render(request,'question.html',{'data':data, 'text1':text1, 'text2':text2, 'text3':text3, 'text4':text4, 'text5':text5, 'text6':text6,'text7':text7,'text8':text8,'text9':text9,'text10':text10,'marks':marks, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'result6': result6, 'result7': result7, 'result8': result8, 'result9': result9, 'result10': result10})
        

def signup(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        form = SignupForm(request.POST)
    
    
        if form.is_valid():
            
            form.save()
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
           
    
            users = User.objects.get(username=username)
       
               
    
        
            
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.add_message(request, messages.SUCCESS,
                                 "Logged in successfull ")
            
            return redirect('/')
           
           
        
            # '127.0.0.1:8000'                                           #get_current_site(request)
           

    else:
        form = SignupForm()
    return render(request, 'index.html', {'form': form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method=='POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
        
         if user is not None:
            messages.add_message(request, messages.SUCCESS,
                                 "Logged in successfull ")
            login(request,user)
            return redirect('/home')
         else:
            messages.add_message(request, messages.ERROR,
                                 "You don't have an account.")
    return render(request,'login2.html',{})

