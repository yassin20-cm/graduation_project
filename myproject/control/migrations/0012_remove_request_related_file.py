# Generated by Django 5.2.1 on 2025-07-09 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0011_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='related_file',
        ),
    ]
