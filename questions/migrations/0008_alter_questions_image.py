# Generated by Django 4.2.7 on 2023-11-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_alter_questions_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, default='/static/media/no-img.jpg', upload_to='guestions/', verbose_name='Изображение'),
        ),
    ]
