# Generated by Django 5.1 on 2024-08-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccounts', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='resent',
            field=models.BooleanField(default=False),
        ),
    ]
