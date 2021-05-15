from django.db import models
from django.contrib.auth.models import AbstractUser
from unixtimestampfield.fields import UnixTimeStampField
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):

    class UserTypeChoices(models.IntegerChoices):
        USER = 1, 'User'
        TEACHER = 2, 'Teacher'

    username = models.EmailField('Логин', unique=True)
    name = models.CharField('Имя', max_length=100, null=True, blank=True)
    last_name = models.CharField(
        'Фамилия', max_length=100, null=True, blank=True)
    user_type = models.IntegerField(
        verbose_name='Тип пользователя', choices=UserTypeChoices.choices)
    birth_date = UnixTimeStampField()
    students_start_age = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    students_end_age = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    def get_ages_range(self):
        return str(self.students_start_age) + ' ' + str(self.students_end_age)

    def get_fio(self):
        if getattr(self, "name", None) and getattr(self, "last_name", None):
            return self.name + ' ' + self.last_name
        else:
            return "Не указаны"

    get_ages_range.short_description = 'Диапазон возраста'
    get_fio.short_description = 'ФИО'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-pk']

    def __str__(self):
        return '{} [{}]'.format(getattr(self.name, "name", ""), self.username)

    @staticmethod
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        user = User.objects.create(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name='Оплативший пользователь',
                             related_name='user_payment', on_delete=models.DO_NOTHING)
    datetime = UnixTimeStampField(verbose_name='Время оплаты', auto_now_add=True)
    amount = models.FloatField(verbose_name='Сумма оплаты')

    class Meta:
        verbose_name = 'Пополнение'
        verbose_name_plural = 'Пополнения'

    def __str__(self):
        return f"{self.pk}-{self.amount}"


class Subscription(models.Model):
    class SubscriptionTypeChoices(models.IntegerChoices):
        BASE = 1, 'Базовая подписка'
        ADVANCED = 2, 'Продвинутая подписка'
        PRO = 3, 'PRO подписка'

    user = models.ForeignKey(
        User, verbose_name='Подписавшийся', related_name='user_subscription', on_delete=models.CASCADE)
    subscription_plan = models.IntegerField(
        'План подписки', choices=SubscriptionTypeChoices.choices, default=1)
    start_date = UnixTimeStampField(verbose_name='Дата начала')
    end_date = UnixTimeStampField(verbose_name='Дата конца', )
    length = models.IntegerField('Длительность в днях')
    paid_amount = models.IntegerField('Сумма оплаты')
    paid = models.BooleanField('Оплачено', default=False)
    finished = models.BooleanField('Завершена', default=False)

    def get_date_range(self):
        return str(self.start_date) + ' -- ' + str(self.end_date)

    get_date_range.short_description = 'Начало конец подписки'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"{self.pk}-{self.user}"
