from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class QuestionandAnswer(models.Model):
        # fields of the model
    subject=models.CharField(max_length=100,unique=True)
    question1=models.TextField()
    question2=models.TextField()
    question3=models.TextField()
    question4=models.TextField()
    question5=models.TextField()
    question6=models.TextField()
    question7=models.TextField()
    question8=models.TextField()
    question9=models.TextField()
    question10=models.TextField()
    answer1=models.TextField()
    answer2=models.TextField()
    answer3=models.TextField()
    answer4=models.TextField()
    answer5=models.TextField()  
    answer6=models.TextField()
    answer7=models.TextField()
    answer8=models.TextField()
    answer9=models.TextField()
    answer10=models.TextField()
    def __str__(self):
        return str(self.subject)
 
        # renames the instances of the model
  
        # with their title name
        
class StudentResult(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=120,null=False)
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
    


 



   