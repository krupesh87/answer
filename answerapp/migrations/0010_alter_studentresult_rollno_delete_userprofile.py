# Generated by Django 4.2 on 2023-04-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answerapp', '0009_studentresult_rollno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='rollno',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
