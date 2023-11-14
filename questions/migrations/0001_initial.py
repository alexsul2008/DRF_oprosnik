# Generated by Django 4.2.7 on 2023-11-14 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Текст ответа')),
                ('approved', models.BooleanField(default=False, help_text='Атрибут указывающий на правильность ответа', verbose_name='Правильность ответа')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='GroupsQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Наименование группы')),
                ('in_active', models.BooleanField(default=True, help_text='Атрибут указывающий выводить/не выводить группу вопросов при прохождении опроса', verbose_name='Активность группы')),
                ('groups', models.ManyToManyField(blank=True, related_name='groups_question', to='auth.group', verbose_name='Группа отдела')),
            ],
            options={
                'verbose_name': 'Группа вопросов',
                'verbose_name_plural': 'Группы вопросов',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Вопрос')),
                ('in_active', models.BooleanField(default=True, help_text='Атрибут указывающий выводить/не выводить вопрос при прохождении опроса', verbose_name='Активность вопроса')),
                ('image', models.ImageField(blank=True, upload_to='guestions/', verbose_name='Изображение')),
                ('doc_url', models.CharField(blank=True, default='', max_length=250, verbose_name='Ссылка на документ')),
                ('groups_questions', models.ManyToManyField(blank=True, related_name='question_group', to='questions.groupsquestions', verbose_name='Группа вопросов')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkPermitUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=150, verbose_name='Сессия пользователя')),
                ('date_passage', models.DateField(auto_now_add=True, verbose_name='Дата прохождения опроса')),
                ('total_questions', models.IntegerField(default=0, null=True, verbose_name='Всего вопросов опроса')),
                ('total_not_correct', models.IntegerField(default=0, null=True, verbose_name='Всего не правильных ответов')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsersAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=150, verbose_name='Сессия пользователя')),
                ('correct', models.BooleanField(default=False, verbose_name='Правильность ответа')),
                ('is_answer', models.BooleanField(default=False, verbose_name='Признак ответа на вопрос')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='auth.group', verbose_name='Группа пользователя')),
                ('otv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='questions.answers', verbose_name='Ответ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_permit_id', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('vop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questions', verbose_name='Вопрос в ответе')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответы пользователей',
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_questions', to='questions.questions'),
        ),
    ]
