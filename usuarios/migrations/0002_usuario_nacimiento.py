# Generated by Django 4.0.4 on 2022-05-30 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nacimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]