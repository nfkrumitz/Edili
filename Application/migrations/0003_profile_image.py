# Generated by Django 3.0 on 2021-11-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile_pics'),
        ),
    ]
