from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .form import SignupForm
from .models import *
# Create your views here.
import pytesseract
def Logout(request):
    logout(request)
    return redirect("/")

from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def Home(request):
    print("hello1")
    if request.user.is_authenticated:
        data=QuestionandAnswer.objects.last()
        
        if request.method == 'POST':   
            dplantsimage = request.POST.get('plantsimage')
            dplantsimage1 = request.POST.get('plantsimage1')
            dplantsimage2 = request.POST.get('plantsimage2')
            dplantsimage3 = request.POST.get('plantsimage3')
            dplantsimage4 = request.POST.get('plantsimage4')
            
        
            text = pytesseract.image_to_string(dplantsimage )   
            print("hii",text)    
    
            answer1=request.POST.get('answer1')
            answer2=request.POST.get('answer2')
            answer3=request.POST.get('answer3')
            answer4=request.POST.get('answer4')
            answer5=request.POST.get('answer5')

           
            
            messages.add_message(request, messages.SUCCESS,
                                 "successfull ")
        return render(request,'home.html',{'data':data})
    

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

