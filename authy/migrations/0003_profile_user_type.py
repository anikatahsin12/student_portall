# Generated by Django 3.2.5 on 2021-08-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_auto_20210726_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=50),
        ),
    ]