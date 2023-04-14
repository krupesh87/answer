# Generated by Django 4.2 on 2023-04-14 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answerapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('Result', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
