# Generated by Django 4.2.7 on 2023-11-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_questions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]