# Generated by Django 4.2 on 2023-04-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answerapp', '0011_questionandanswer_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswer',
            name='subject',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
