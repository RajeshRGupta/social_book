# Generated by Django 5.1 on 2024-08-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_alter_books_b_cost_alter_books_b_year_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='b_visibility',
            field=models.BooleanField(default=True),
        ),
    ]
