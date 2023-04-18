from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class QuestionandAnswer(models.Model):
        # fields of the model
    subject=models.CharField(max_length=100,unique=True)
    question1=models.CharField(max_length=500)
    question2=models.CharField(max_length=500)
    question3=models.CharField(max_length=500)
    question4=models.CharField(max_length=500)
    question5=models.CharField(max_length=500)
    question6=models.CharField(max_length=500)
    question7=models.CharField(max_length=500)
    question8=models.CharField(max_length=500)
    question9=models.CharField(max_length=500)
    question10=models.CharField(max_length=500)
    answer1=models.CharField(max_length=500)
    answer2=models.CharField(max_length=500)
    answer3=models.CharField(max_length=500)
    answer4=models.CharField(max_length=500)
    answer5=models.CharField(max_length=500)  
    answer6=models.CharField(max_length=500)
    answer7=models.CharField(max_length=500)
    answer8=models.CharField(max_length=500)
    answer9=models.CharField(max_length=500)
    answer10=models.CharField(max_length=500)
    def __str__(self):
        return str(self.subject)
 
        # renames the instances of the model
        # with their title name
class StudentResult(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    answer1=models.CharField(max_length=500)
    answer2=models.CharField(max_length=500)
    answer3=models.CharField(max_length=500)
    answer4=models.CharField(max_length=500)
    answer5=models.CharField(max_length=500)  
    answer6=models.CharField(max_length=500)
    answer7=models.CharField(max_length=500)
    answer8=models.CharField(max_length=500)
    answer9=models.CharField(max_length=500)
    answer10=models.CharField(max_length=500)
    Result=models.CharField(max_length=500)
    rollno = models.PositiveIntegerField()
    def __str__(self):
        return str(self.rollno)
    


 



   