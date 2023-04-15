from django.contrib import admin

# Register your models here.
from .models import QuestionandAnswer,StudentResult

   
admin.site.register(QuestionandAnswer)
admin.site.register(StudentResult)
