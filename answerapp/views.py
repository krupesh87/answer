from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .form import SignupForm
# Create your views here.
# def index(request):
#     form = UserCreationForm()
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password1']
#         print(username,password)
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user = authenticate(request, username=username, password=password)
#             login(request,user)
            
#             messages.add_message(request, messages.SUCCESS,
#                                  "Logged in successfull ")
#             return redirect('/login/')
           
           

#         else:
#             messages.add_message(request, messages.SUCCESS,
#                                  "Somethingwent wrong ")
#             form = UserCreationForm()
#     return render(request,'index.html',{'form':form})


def Home(request):
    return render(request,'home.html')
def index(request):
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
            return redirect('/login/')
           
           
        
            # '127.0.0.1:8000'                                           #get_current_site(request)
           

    else:
        form = SignupForm()
    return render(request, 'index.html', {'form': form},{})


def Login(request):
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

