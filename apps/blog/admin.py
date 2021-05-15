from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_created',  'accessory_level')
    list_display_links = ('name',)
    filter_fields = ('accessory_level', )
    search_fields = ('name',)
    order_by = ('-date_created', '-pk')
    filter_horizontal = ('attachment', )
