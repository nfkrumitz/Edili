# Generated by Django 3.0 on 2022-03-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0012_auto_20220306_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='target',
            field=models.TextField(null=True),
        ),
    ]
