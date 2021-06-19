from django.contrib import admin, messages
from mptt.admin import TreeRelatedFieldListFilter
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from admin_actions.admin import ActionsModelAdmin
from .models import (
    Card,
    PurchasedCard,
    Group,
    Plan,
    Collection,
    PlanCard,
    Handbook,
)


def set_value(card: Card, value: bool, request):
    card.published = value
    card.save()
    return HttpResponseRedirect(reverse_lazy('admin:lessons_card_changelist'), request)


@admin.register(Handbook)
class HandbookAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'get_learning_themes',
        'get_education_process',
        'get_learning_types'
    )
    filter_horizontal = (
        'learning_themes',
        'learning_types',
        'education_process',
    )
    list_filter = (
        ('learning_themes', TreeRelatedFieldListFilter),
        ('learning_types', TreeRelatedFieldListFilter),
        ('education_process', TreeRelatedFieldListFilter),
    )


@admin.register(PlanCard)
class PlanCardAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'plan',
        'card',
        'order'
    )
    list_filter = 'plan',
    search_fields = ('plan__name', 'card__name')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'name',
        'user',
        'get_collection_cards'
    )
    list_display_links = 'name',
    search_fields = ('user__username', 'name', 'cards__name')
    filter_horizontal = 'cards',


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = (
        'name',
        'user',
        'get_plan_cards',
        'get_plan_groups'
    )
    list_display_links = 'name',
    search_fields = ('user__username', 'cards__name', 'name')
    filter_horizontal = (
        'cards',
        'groups',
    )


@admin.register(PurchasedCard)
class PurchasedCardAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = (
        'user',
        'card'
    )
    search_fields = ('user__username', 'card__name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = (
        'name',
        'user',
        'duration'
    )
    list_display_links = 'name',
    search_fields = ('name', 'user__username', 'card__name')


@admin.register(Card)
class CardAdmin(ActionsModelAdmin):
    list_per_page = 50
    list_display = (
        'admin_photo',
        'name',
        'valute_price',
        'accessory_level',
        'get_learning_range',
        'get_learning_themes',
        'get_learning_subjects',
        'get_learning_types',
        'get_education_process',
        'published',
    )
    list_display_links = 'name',
    list_filter = (
        ('learning_themes', TreeRelatedFieldListFilter),
        ('learning_subjects', TreeRelatedFieldListFilter),
        ('learning_types', TreeRelatedFieldListFilter),
        ('education_process', TreeRelatedFieldListFilter),
        'published',
    )
    search_fields = 'name',
    filter_horizontal = (
        'images',
        'learning_range',
        'learning_themes',
        'learning_subjects',
        'learning_types',
        'education_process',
        'favourites'
    )
    actions_row = actions_detail = 'publish_card', 'hide_card',

    def publish_card(self, request, pk):
        card = Card.objects.get(pk=pk)
        if card.published:
            messages.error(
                request, 'Карточка уже опубликована')
            return HttpResponseRedirect(reverse_lazy('admin:lessons_card_changelist'), request)
        else:
            messages.success(
                request, 'Карточка опубликована')
            return set_value(card, True, request)

    def hide_card(self, request, pk):
        card = Card.objects.get(pk=pk)
        if not card.published:
            messages.error(
                request, 'Карточка уже спрятана')
            return HttpResponseRedirect(reverse_lazy('admin:lessons_card_changelist'), request)
        else:
            messages.success(
                request, 'Карточка спрятана')
            return set_value(card, False, request)

    publish_card.short_description = 'Опубликовать'
    publish_card.url_path = 'publish-card'
    hide_card.short_description = 'Спрятать'
    hide_card.url_path = 'hide-card'
