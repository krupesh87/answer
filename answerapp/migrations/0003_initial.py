# Generated by Django 4.1.7 on 2023-03-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('answerapp', '0002_delete_questionandanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionandAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(max_length=500)),
                ('question2', models.CharField(max_length=500)),
                ('question3', models.CharField(max_length=500)),
                ('question4', models.CharField(max_length=500)),
                ('question5', models.CharField(max_length=500)),
                ('question6', models.CharField(max_length=500)),
                ('question7', models.CharField(max_length=500)),
                ('question8', models.CharField(max_length=500)),
                ('question9', models.CharField(max_length=500)),
                ('question10', models.CharField(max_length=500)),
                ('answer1', models.CharField(max_length=500)),
                ('answer2', models.CharField(max_length=500)),
                ('answer3', models.CharField(max_length=500)),
                ('answer4', models.CharField(max_length=500)),
                ('answer5', models.CharField(max_length=500)),
                ('answer6', models.CharField(max_length=500)),
                ('answer7', models.CharField(max_length=500)),
                ('answer8', models.CharField(max_length=500)),
                ('answer9', models.CharField(max_length=500)),
                ('answer10', models.CharField(max_length=500)),
            ],
        ),
    ]