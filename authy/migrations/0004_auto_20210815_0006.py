# Generated by Django 3.2.5 on 2021-08-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0003_profile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='plans',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='topic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='url1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
