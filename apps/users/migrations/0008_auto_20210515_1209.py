# Generated by Django 3.1.8 on 2021-05-15 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_subscription_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=unixtimestampfield.fields.UnixTimeStampField(verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=unixtimestampfield.fields.UnixTimeStampField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscription', to=settings.AUTH_USER_MODEL, verbose_name='Подписавшийся'),
        ),
    ]
