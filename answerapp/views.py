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
        data=QuestionandAnswer.objects.last()
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
        
        if request.method == 'POST':   
            dplantsimage = request.POST.get('plantsimage')
            dplantsimage1 = request.POST.get('plantsimage1')
            dplantsimage2 = request.POST.get('plantsimage2')
            dplantsimage3 = request.POST.get('plantsimage3')
            dplantsimage4 = request.POST.get('plantsimage4')
            dplantsimage5 = request.POST.get('plantsimage5')
            dplantsimage6 = request.POST.get('plantsimage6')
            dplantsimage7 = request.POST.get('plantsimage7')
            dplantsimage8 = request.POST.get('plantsimage8')
            dplantsimage9 = request.POST.get('plantsimage9')

            if dplantsimage:
                text1 = pytesseract.image_to_string(dplantsimage)  
                text2 = pytesseract.image_to_string(dplantsimage1)
                text3 = pytesseract.image_to_string(dplantsimage2)
                text4 = pytesseract.image_to_string(dplantsimage3)
                text5 = pytesseract.image_to_string(dplantsimage4)  
                text6 = pytesseract.image_to_string(dplantsimage5)  
                text7 = pytesseract.image_to_string(dplantsimage6)  
                text8 = pytesseract.image_to_string(dplantsimage7)  
                text9= pytesseract.image_to_string(dplantsimage8)  
                text10 = pytesseract.image_to_string(dplantsimage9)  
            else:
                print(text1)
    
            answer1=request.POST.get('answer1')
            answer2=request.POST.get('answer2')
            answer3=request.POST.get('answer3')
            answer4=request.POST.get('answer4')
            answer5=request.POST.get('answer5')
            answer6=request.POST.get('answer6')
            answer7=request.POST.get('answer7')
            answer8=request.POST.get('answer8')
            answer9=request.POST.get('answer9')
            answer10=request.POST.get('answer10')

            dat=QuestionandAnswer.objects.last()
            
            if(answer1):
                 result1=SequenceMatcher(None, dat.answer1, answer1).ratio()
                 result2=SequenceMatcher(None, dat.answer2, answer2).ratio()
                 result3=SequenceMatcher(None, dat.answer3, answer3).ratio()
                 result4=SequenceMatcher(None, dat.answer4, answer4).ratio()
                 result5=SequenceMatcher(None, dat.answer5, answer5).ratio()
                 result6=SequenceMatcher(None, dat.answer6, answer6).ratio()
                 result7=SequenceMatcher(None, dat.answer7, answer7).ratio()
                 result8=SequenceMatcher(None, dat.answer8, answer8).ratio()
                 result9=SequenceMatcher(None, dat.answer9, answer9).ratio()
                 result10=SequenceMatcher(None, dat.answer10, answer10).ratio()
                 marks=math.ceil((result1+result2+result3+result4+result5+result6+result7+result8+result9+result10)*100/5)
                 print(marks)           
            
            messages.add_message(request, messages.SUCCESS,
                                 "successfull ")
        return render(request,'home.html',{'data':data, 'text1':text1, 'text2':text2, 'text3':text3, 'text4':text4, 'text5':text5, 'text6':text6,'text7':text7,'text8':text8,'text9':text9,'text10':text10,'marks':marks})
    

    return redirect('login') 
    
def signup(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
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

