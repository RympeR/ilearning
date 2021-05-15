import os
from django.db import models
from django.utils.safestring import mark_safe
from apps.utils.func import attachments
from mptt.models import MPTTModel, TreeForeignKey

ATTACHMENT_TYPE_CHOICES = (
    ('IMAGE', 'Изображение'),
    ('VIDEO', 'Видео'),
    ('AUDIO', 'Аудио'),
    ('DOCUMENT', 'Документ'),
    ('PRESENTATION', 'Презентация'),
)

LANGUAGE_CHOICES = (
    ('UK', 'UK'),
    ('RU', 'RU'),
    ('EN', 'EN'),
)


class TaskTypes(models.Model):
    name = models.CharField('Task type', max_length=100)
    language = models.CharField(
        'Task language', max_length=2, choices=LANGUAGE_CHOICES)
    icon = models.ImageField('Type icon')
    slug = models.SlugField()
    display = models.BooleanField('Отобразить', default=True)

    def admin_photo(self):
        if hasattr(self.icon, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.icon.url))
        return None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Типы заданий'


class LearningRange(models.Model):
    name = models.CharField('Название', max_length=100)
    language = models.CharField(
        'Range language', max_length=2, choices=LANGUAGE_CHOICES)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}--{self.language}"

    class Meta:
        verbose_name = 'Диапазон обучения'
        verbose_name_plural = 'Диапазоны обучения'


class LearningSubjects(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='parent_category', blank=True, null=True, related_name='parent_category', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    language = models.CharField(
        'Язык', max_length=2, choices=LANGUAGE_CHOICES)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}--{self.language}"

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'Подкатегория предмета'

    class Meta:
        verbose_name = 'Изучаемый предмет'
        verbose_name_plural = 'Изучаемые предметы'


class LessonTheme(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='lesson_theme_parent', blank=True, null=True, related_name='lesson_theme_parent', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    language = models.CharField(
        'Язык', max_length=2, choices=LANGUAGE_CHOICES)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}--{self.language}"

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'Подкатегория темы занятия'

    class Meta:
        verbose_name = 'Тема урока'
        verbose_name_plural = 'Темы уроков'


class LessonTypes(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='lesson_types', blank=True, null=True, related_name='lesson_types_parent', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=100)
    language = models.CharField(
        'Язык', max_length=2, choices=LANGUAGE_CHOICES)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}--{self.language}"

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'Подкатегория типа занятия'

    class Meta:
        verbose_name = 'Тип урока'
        verbose_name_plural = 'Типы уроков'


class EducationProcesses(MPTTModel):
    parent = TreeForeignKey(
        'self', verbose_name='education_process', blank=True, null=True, related_name='education_process_parent', on_delete=models.CASCADE)
    name = models.CharField('Subject name', max_length=100)
    language = models.CharField(
        'Язык', max_length=2, choices=LANGUAGE_CHOICES)
    display = models.BooleanField('Отобразить', default=True)

    def __str__(self):
        return f"{self.name}--{self.language}"

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'Подкатегория образовательного процесса'

    class Meta:
        verbose_name = 'Познавательный процесс'
        verbose_name_plural = 'Познавательные процессы'


class Attachment(models.Model):
    type = models.CharField(verbose_name='Тип файла',
                            max_length=15, choices=ATTACHMENT_TYPE_CHOICES)
    file = models.FileField(verbose_name='Вложение', upload_to=attachments)
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    filename.short_description = 'Название файла'
    
    def __str__(self):
        return f"{self.type}--{self.filename()}"

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'
