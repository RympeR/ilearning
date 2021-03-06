# Generated by Django 3.1.8 on 2021-05-13 05:35

import apps.utils.func
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IMAGE', 'Изображение'), ('VIDEO', 'Видео'), ('AUDIO', 'Аудио'), ('DOCUMENT', 'Документ')], max_length=15, verbose_name='Тип файла')),
                ('file', models.FileField(upload_to=apps.utils.func.attachments, verbose_name='Вложение')),
            ],
            options={
                'verbose_name': 'Вложение',
                'verbose_name_plural': 'Вложения',
            },
        ),
        migrations.CreateModel(
            name='LearningRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Range language')),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
            ],
            options={
                'verbose_name': 'Диапазон обучения',
                'verbose_name_plural': 'Диапазоны обучения',
            },
        ),
        migrations.CreateModel(
            name='TaskTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Task type')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Task language')),
                ('icon', models.ImageField(upload_to='', verbose_name='Type icon')),
                ('slug', models.SlugField()),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
            ],
            options={
                'verbose_name': 'Тип задания',
                'verbose_name_plural': 'Типы заданий',
            },
        ),
        migrations.CreateModel(
            name='LessonTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Язык')),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('Подкатегория типа занятия', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_types_parent', to='info.lessontypes', verbose_name='lesson_types')),
            ],
            options={
                'verbose_name': 'Тип урока',
                'verbose_name_plural': 'Типы уроков',
            },
        ),
        migrations.CreateModel(
            name='LessonTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Язык')),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('Подкатегория темы занятия', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_theme_parent', to='info.lessontheme', verbose_name='lesson_theme_parent')),
            ],
            options={
                'verbose_name': 'Тема урока',
                'verbose_name_plural': 'Темы уроков',
            },
        ),
        migrations.CreateModel(
            name='LearningSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Язык')),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('Подкатегория предмета', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='info.learningsubjects', verbose_name='parent_category')),
            ],
            options={
                'verbose_name': 'Изучаемый предмет',
                'verbose_name_plural': 'Изучаемые предметы',
            },
        ),
        migrations.CreateModel(
            name='EducationProcesses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Subject name')),
                ('language', models.CharField(choices=[('UK', 'UK'), ('RU', 'RU'), ('EN', 'EN')], max_length=2, verbose_name='Язык')),
                ('display', models.BooleanField(default=True, verbose_name='Отображезить')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('Подкатегория образовательного процесса', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_process_parent', to='info.educationprocesses', verbose_name='education_process')),
            ],
            options={
                'verbose_name': 'Образовательный процесс',
                'verbose_name_plural': 'Образовательные процессы',
            },
        ),
    ]
