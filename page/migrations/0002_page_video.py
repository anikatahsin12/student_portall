# Generated by Django 3.2.5 on 2021-07-16 08:41

from django.db import migrations, models
import page.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=page.models.user_directory_path, verbose_name='Video'),
        ),
    ]
