from django.contrib import admin
from django.contrib.admin.filters import AllValuesFieldListFilter
from django.contrib.admin import DateFieldListFilter
from .models import (
    User,
    Payment,
    Subscription,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'username',
        'get_fio',
        'user_type'
    )
    list_display_links = 'username',
    list_filter = (
        'user_type',
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'user',
        'datetime',
        'amount',
    )
    search_fields = 'user__username',
    list_filter = (
        ('datetime', DateFieldListFilter),
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'pk',
        'user',
        'subscription_plan',
        'paid_amount',
        'length',
        'get_date_range',
    )
    list_display_links = 'pk',
    search_fields = ('user__username', )
    list_filter = (
        'subscription_plan',
        'paid',
        'finished',
        ('start_date', DateFieldListFilter),
        ('end_date', DateFieldListFilter),
    )
