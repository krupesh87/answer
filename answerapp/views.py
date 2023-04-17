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
    dataw=StudentResult.objects.filter(username=request.user)

    
    if request.user.is_authenticated and not dataw:    
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
            if dplantsimage1:  
                text2 = pytesseract.image_to_string(dplantsimage1)
            if dplantsimage2:
                text3 = pytesseract.image_to_string(dplantsimage2)
            if dplantsimage3:
                text4 = pytesseract.image_to_string(dplantsimage3)
            if dplantsimage4:
                text5 = pytesseract.image_to_string(dplantsimage4)  
            if dplantsimage5:
                text6 = pytesseract.image_to_string(dplantsimage5) 
            if dplantsimage6: 
                text7 = pytesseract.image_to_string(dplantsimage6)  
            if dplantsimage7:
                text8 = pytesseract.image_to_string(dplantsimage7)  
            if dplantsimage8:
                text9= pytesseract.image_to_string(dplantsimage8)  
            if dplantsimage9:
                text10 = pytesseract.image_to_string(dplantsimage9)  
          
    
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
            rollno=request.POST.get('rollno')

            dat=QuestionandAnswer.objects.last()
            
            if(answer1 or answer2 or answer3 or answer4 or answer5 or answer6 or answer7 or answer8 or answer9 or answer10):
                result1=round(SequenceMatcher(None, dat.answer1, answer1).ratio(),3)
                result2=round(SequenceMatcher(None, dat.answer2, answer2).ratio(),3)
                result3=round(SequenceMatcher(None, dat.answer3, answer3).ratio(),3)
                result4=round(SequenceMatcher(None, dat.answer4, answer4).ratio(),3)
                result5=round(SequenceMatcher(None, dat.answer5, answer5).ratio(),3)
                result6=round(SequenceMatcher(None, dat.answer6, answer6).ratio(),3)
                result7=(round((SequenceMatcher(None, dat.answer7, answer7).ratio()),3))
                result8=round(SequenceMatcher(None, dat.answer8, answer8).ratio(),3)
                result9=round(SequenceMatcher(None, dat.answer9, answer9).ratio(),3)
                result10=round(SequenceMatcher(None, dat.answer10, answer10).ratio(),3)
                marks=math.floor((result1+result2+result3+result4+result5+result6+result7+result8+result9+result10)*100/10)

               
         
                resultsmain=StudentResult(username=request.user,rollno=rollno,answer1=result1,answer2=result2,answer3=result3,answer4=result4,answer5=result5,answer6=result6,answer7=result7,answer8=result8,answer9=result9,answer10=result10,Result=marks)
                resultsmain.save()
                
                messages.add_message(request, messages.SUCCESS,
                                 "successfull ")
                return redirect('home')
        return render(request,'home.html',{'data':data, 'text1':text1, 'text2':text2, 'text3':text3, 'text4':text4, 'text5':text5, 'text6':text6,'text7':text7,'text8':text8,'text9':text9,'text10':text10,'marks':marks, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4, 'result5': result5, 'result6': result6, 'result7': result7, 'result8': result8, 'result9': result9, 'result10': result10})
    elif(dataw):
        return render(request,'home.html',{'dataw':dataw[0]})   
       
        
          
            
          
       
    

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

