from django.db import models
from django.db.models import Max
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from apps.utils.func import card_attachment
from apps.info.models import *
from apps.users.models import *

LANGUAGE_CHOICES = (
    ('UK', 'UK'),
    ('RU', 'RU'),
    ('EN', 'EN'),
)

VALUTE_CHOICES = (
    ('USD', 'USD'),
    ('UAH', 'UAH'),
    ('RUB', 'RUB'),
)


class Card(models.Model):

    class AcessoryLevel(models.IntegerChoices):
        BASE = 1, 'Покупка'
        ADVANCED = 2, 'Подписка'
        PRO = 3, 'PRO  аккаунт'

    name = models.CharField('Название карточки', max_length=100)
    slug = models.SlugField('Слаг')
    card_type = models.ForeignKey(
        TaskTypes, verbose_name='card_type', related_name='card_type', on_delete=models.DO_NOTHING, null=True, blank=True)
    images = models.ManyToManyField(
        Attachment, related_name='card_image_attachments', blank=True)
    preview = models.ImageField(
        verbose_name='Превью карточки', upload_to=card_attachment, blank=True, null=True)
    short_description = HTMLField(
        verbose_name='Краткое описание', blank=True, null=True)
    full_description = HTMLField(
        verbose_name='Полное описание', blank=True, null=True)
    price = models.FloatField('Цена')
    valute = models.CharField(verbose_name='Валюта',
                              max_length=3, choices=VALUTE_CHOICES)
    attachment = models.FileField(
        verbose_name='Вложение', upload_to=card_attachment, blank=True, null=True)
    video = models.FileField(verbose_name='Вложенное видео',
                             upload_to=card_attachment, blank=True, null=True)
    hosting_url = models.URLField(
        verbose_name='Ссылка на видеохостинге', blank=True, null=True)
    accessory_level = models.CharField(
        'Уровень доступа', choices=AcessoryLevel.choices, max_length=10)
    learning_range = models.ManyToManyField(
        LearningRange, verbose_name='Периоды обучения', related_name='card_leargning_range')
    learning_themes = models.ManyToManyField(
        LessonTheme, verbose_name='Темы занятия', related_name='card_leargning_theme')
    learning_subjects = models.ManyToManyField(
        LearningSubjects, verbose_name='Предметы карточки', related_name='card_leargning_subjects')
    learning_types = models.ManyToManyField(
        LessonTypes, verbose_name='Виды задания ', related_name='card_leargning_type')
    education_process = models.ManyToManyField(
        EducationProcesses, verbose_name='Познавательные процессы', related_name='card_education_process')
    favourites = models.ManyToManyField(
        User, verbose_name='Избранное людей', related_name='favourites_card', blank=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=False)

    def admin_photo(self):
        if hasattr(self.preview, 'url'):
            return mark_safe('<img src="{}" width="100" /'.format(self.preview.url))
        return None

    def get_learning_range(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_range.all()])

    def get_learning_themes(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_themes.all()])

    def get_learning_subjects(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_subjects.all()])

    def get_learning_types(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_types.all()])

    def get_education_process(self):
        return "\n".join([f'{p.name} || ' for p in self.education_process.all()])

    def valute_price(self):
        return f'{self.price} {self.valute}'

    get_learning_range.short_description = 'Возростной диапазон'
    get_learning_themes.short_description = 'Темы для изучения'
    get_learning_subjects.short_description = 'Предметы изучения'
    get_learning_types.short_description = 'Типы обучения'
    get_education_process.short_description = 'Познавательные процессы'
    admin_photo.short_description = 'Превью'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


class PurchasedCard(models.Model):
    user = models.ForeignKey(
        User, related_name='user_purcased_card', verbose_name='Покупатель', on_delete=models.CASCADE)
    card = models.ForeignKey(
        Card, related_name='card_purcased_card', verbose_name='Карточка', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}-{self.user}-{self.card}'

    class Meta:
        verbose_name = 'Купленная карточка'
        verbose_name_plural = 'Купленные карточки'
        unique_together = ('user', 'card')


class Group(models.Model):
    name = models.CharField('Название', max_length=100)
    user = models.ForeignKey(
        User, related_name='user_group', verbose_name='Создатель', on_delete=models.CASCADE)
    duration = models.CharField('Длительность', max_length=100)
    age = models.CharField('Возраст', max_length=100)

    def __str__(self):
        return f'{self.name} || {self.user} - {self.age} : {self.duration}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        unique_together = ('name', 'user',)


class Plan(models.Model):
    name = models.CharField('Название плана', max_length=100)
    user = models.ForeignKey(
        User, related_name='user_plan', verbose_name='Создатель', on_delete=models.CASCADE)
    cards = models.ManyToManyField(
        Card, verbose_name='Карточки', related_name='plan_cards', through='PlanCard')
    groups = models.ManyToManyField(
        Group, verbose_name='Группы плана', related_name='plan_groups')

    def __str__(self):
        return str(self.user) + '--' + self.name

    def get_plan_groups(self):
        return "\n".join([f'{p.name} || ' for p in self.groups.all()])

    def get_plan_cards(self):
        return "\n".join([f'{p.name} || ' for p in self.cards.all()])

    get_plan_groups.short_description = 'Группы плана'
    get_plan_cards.short_description = 'Карточки в плане'

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'
        unique_together = ('name', 'user',)


class Collection(models.Model):
    name = models.CharField('Название коллекции', max_length=100)
    user = models.ForeignKey(
        User, related_name='user_collection', verbose_name='Создатель', on_delete=models.CASCADE)
    cards = models.ManyToManyField(
        Card, verbose_name='Карточки в коллекции', related_name='collection_card')

    def get_collection_cards(self):
        return "\n".join([f'{p.name} || ' for p in self.cards.all()])

    get_collection_cards.short_description = 'Карточки в коллекции'

    def __str__(self):
        return self.name + '--' + str(self.user)

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        unique_together = ('user', 'name')


class PlanCard(models.Model):
    plan = models.ForeignKey(
        Plan, related_name='plan_plancard', verbose_name='План карточки', on_delete=models.CASCADE)
    card = models.ForeignKey(
        Card, related_name='card_plancard', verbose_name='Карточка плана', on_delete=models.DO_NOTHING)
    order = models.IntegerField('Порядковый номер в плане')

    def __str__(self):
        return f'{self.plan} - {self.card} : {self.order}'

    class Meta:
        verbose_name = 'Карточка в плане'
        verbose_name_plural = 'Карточки в плане'
        unique_together = ('plan', 'card', 'order')


class Handbook(models.Model):
    learning_themes = models.ManyToManyField(
        LessonTheme, verbose_name='Темы занятия', related_name='handbook_leargning_theme')
    learning_types = models.ManyToManyField(
        LessonTypes, verbose_name='Виды задания', related_name='handbook_leargning_type')
    education_process = models.ManyToManyField(
        EducationProcesses, verbose_name='Познавательные процессы', related_name='handbook_education_process')

    def get_education_process(self):
        return "\n".join([f'{p.name} || ' for p in self.education_process.all()])

    def get_learning_types(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_types.all()])

    def get_learning_themes(self):
        return "\n".join([f'{p.name} || ' for p in self.learning_themes.all()])

    get_education_process.short_description = 'Образовательные процссе'
    get_learning_types.short_description = 'Типы обучения'
    get_learning_themes.short_description = 'Познавательные процессы'

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


@receiver(post_delete, sender=PlanCard, dispatch_uid='plan_card_delete_signal')
def log_deleted_plancard(sender, instance, using, **kwargs):
    qs = PlanCard.objects.filter(plan=instance.plan)
    for ind, card in enumerate(qs):
        card.order = ind + 1
        card.save()


@receiver(pre_save, sender=PlanCard, dispatch_uid='plan_card_update_signal')
def log_updated_plancard(sender, instance, created, **kwargs):
    if created:
        plan_card = PlanCard.objects.filter(
            plan=instance.plan).aggregate(Max('order'))['order__max']
        print(plan_card)
        instance.order = plan_card.order + 1
        instance.save()
    else:
        plan_card = PlanCard.objects.get(
            plan=instance.plan, order=instance.order-1)
        plan_card.order, instance.order = instance.order, plan_card.order
        plan_card.save()
        instance.save()
