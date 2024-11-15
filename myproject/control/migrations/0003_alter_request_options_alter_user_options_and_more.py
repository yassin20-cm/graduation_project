# Generated by Django 5.1.2 on 2024-11-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_name']},
        ),
        migrations.AlterField(
            model_name='request',
            name='related_file',
            field=models.FileField(upload_to='request_files/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='templates/one.png', null=True, upload_to='profiles/%y/%m/%d'),
        ),
    ]
