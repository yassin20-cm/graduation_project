# Generated by Django 5.2.1 on 2025-07-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0009_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='/profiles/default.jpg', null=True, upload_to='profiles/%y/%m/%d'),
        ),
    ]
