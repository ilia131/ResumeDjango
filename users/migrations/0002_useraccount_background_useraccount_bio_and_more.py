# Generated by Django 4.2.6 on 2024-04-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='background',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
