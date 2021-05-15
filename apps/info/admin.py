from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

from .models import (
    TaskTypes,
    LearningRange,
    LearningSubjects,
    LessonTheme,
    LessonTypes,
    EducationProcesses,
    Attachment,
)


@admin.register(TaskTypes)
class TaskTypesAdmin(admin.ModelAdmin):
    list_display = ('admin_photo', 'name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)


@admin.register(LearningRange)
class LearningRangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_display_links = ('type',)
    filter_fields = ('type', )


@admin.register(LearningSubjects, LessonTheme, LessonTypes, EducationProcesses)
class TemplateAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
