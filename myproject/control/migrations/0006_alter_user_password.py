# Generated by Django 5.1.2 on 2024-12-07 16:08

import control.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_remove_user_user_password_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[control.models.validate_password_length]),
        ),
    ]
