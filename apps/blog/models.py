from django.db import models
from apps.info.models import Attachment
from unixtimestampfield.fields import UnixTimeStampField


class Post(models.Model):
    class AccessoryLevel(models.IntegerChoices):
        FREE = 1, 'Бесплатный'
        SUBSCRIBE = 2, 'По подписке'
        
    name = models.CharField(verbose_name='Название', max_length=200)
    slug = models.SlugField(verbose_name='Кодовое название')
    attachment = models.ManyToManyField(
        Attachment, related_name='post_attachment', verbose_name='Вложения')
    date_created = UnixTimeStampField(auto_now_add=True)
    accessory_level = models.IntegerField(
        verbose_name='Уровень доступа', choices=AccessoryLevel.choices)
    hosting_url = models.URLField(
        verbose_name='Ссылка на видеохостинге', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-date_created']
