# Generated by Django 3.2.5 on 2021-08-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
