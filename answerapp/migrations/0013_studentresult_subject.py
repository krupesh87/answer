# Generated by Django 4.2 on 2023-04-18 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('answerapp', '0012_alter_questionandanswer_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]