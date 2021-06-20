from django.contrib import admin, messages
from mptt.admin import TreeRelatedFieldListFilter
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from admin_actions.admin import ActionsModelAdmin
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
class TaskTypesAdmin(ActionsModelAdmin):
    list_display = ('admin_photo', 'name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)
    actions_row = actions_detail = 'display_task_type', 'hide_task_type',

    def display_task_type(self, request, pk):
        task_type = TaskTypes.objects.get(pk=pk)
        if task_type.display:
            messages.error(
                request, 'Тип задания уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_tasktypes_changelist'), request)
        else:
            messages.success(
                request, 'Тип задания опубликован')
            task_type.display = True
            task_type.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_tasktypes_changelist'), request)

    def hide_task_type(self, request, pk):
        task_type = TaskTypes.objects.get(pk=pk)
        if not task_type.display:
            messages.error(
                request, 'Тип задания уже спрятан')
            return HttpResponseRedirect(reverse_lazy('admin:info_tasktypes_changelist'), request)
        else:
            messages.success(
                request, 'Тип задания спрятан')
            task_type.display = False
            task_type.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_tasktypes_changelist'), request)

    display_task_type.short_description = 'Опубликовать'
    display_task_type.url_path = 'publish-task-type'
    hide_task_type.short_description = 'Спрятать'
    hide_task_type.url_path = 'hide-task-type'


@admin.register(LearningRange)
class LearningRangeAdmin(ActionsModelAdmin):
    list_display = ('name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)
    actions_row = actions_detail = 'display_learning_range', 'hide_learning_range',

    def display_learning_range(self, request, pk):
        learning_range = LearningRange.objects.get(pk=pk)
        if learning_range.display:
            messages.error(
                request, 'Пероид обучения уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_learningrange_changelist'), request)
        else:
            messages.success(
                request, 'Пероид обучения опубликован')
            learning_range.display = True
            learning_range.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_learningrange_changelist'), request)

    def hide_learning_range(self, request, pk):
        learning_range = LearningRange.objects.get(pk=pk)
        if not learning_range.display:
            messages.error(
                request, 'Пероид обучения уже спрятан')
            return HttpResponseRedirect(reverse_lazy('admin:info_learningrange_changelist'), request)
        else:
            messages.success(
                request, 'Пероид обучения спрятан')
            learning_range.display = False
            learning_range.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_learningrange_changelist'), request)

    display_learning_range.short_description = 'Опубликовать'
    display_learning_range.url_path = 'publish-learning-range'
    hide_learning_range.short_description = 'Спрятать'
    hide_learning_range.url_path = 'hide-learning-range'


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = 'filename', 'type',
    list_display_links = 'filename',
    list_filter = 'type',


@admin.register(LearningSubjects)
class LearningSubjectsAdmin(ActionsModelAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
    actions_row = actions_detail = 'display_learning_subject', 'hide_learning_subject',

    def display_learning_subject(self, request, pk):
        learning_subject = LearningSubjects.objects.get(pk=pk)
        if learning_subject.display:
            messages.error(
                request, 'Предмет обучения уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_learningsubjects_changelist'), request)
        else:
            messages.success(
                request, 'Предмет обучения опубликован')
            learning_subject.display = True
            learning_subject.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_learningsubjects_changelist'), request)

    def hide_learning_subject(self, request, pk):
        learning_subject = LearningSubjects.objects.get(pk=pk)
        if not learning_subject.display:
            messages.error(
                request, 'Предмет обучения уже спрятан')
            return HttpResponseRedirect(reverse_lazy('admin:info_learningsubjects_changelist'), request)
        else:
            messages.success(
                request, 'Предмет обучения спрятан')
            learning_subject.display = False
            learning_subject.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_learningsubjects_changelist'), request)

    display_learning_subject.short_description = 'Опубликовать'
    display_learning_subject.url_path = 'publish-learning-subject'
    hide_learning_subject.short_description = 'Спрятать'
    hide_learning_subject.url_path = 'hide-learning-subject'


@admin.register(LessonTheme)
class LessonThemeAdmin(ActionsModelAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'language', 'display')
    list_display_links = 'name',
    filter_fields = 'language', 'display'
    search_fields = 'name',
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
    actions_row = actions_detail = 'display_lesson_theme', 'hide_lesson_theme',

    def display_lesson_theme(self, request, pk):
        lesson_theme = LessonTheme.objects.get(pk=pk)
        if lesson_theme.display:
            messages.error(
                request, 'Тема урока уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontheme_changelist'), request)
        else:
            messages.success(
                request, 'Тема урока опубликована')
            lesson_theme.display = True
            lesson_theme.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontheme_changelist'), request)

    def hide_lesson_theme(self, request, pk):
        lesson_theme = LessonTheme.objects.get(pk=pk)
        if not lesson_theme.display:
            messages.error(
                request, 'Тема урока уже спрятана')
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontheme_changelist'), request)
        else:
            messages.success(
                request, 'Тема урока спрятана')
            lesson_theme.display = False
            lesson_theme.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontheme_changelist'), request)

    display_lesson_theme.short_description = 'Опубликовать'
    display_lesson_theme.url_path = 'publish-lesson-theme'
    hide_lesson_theme.short_description = 'Спрятать'
    hide_lesson_theme.url_path = 'hide-lesson-theme'


@admin.register(LessonTypes)
class LessonTypesAdmin(ActionsModelAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'language', 'display')
    list_display_links = 'name',
    filter_fields = 'language', 'display'
    search_fields = 'name',
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
    actions_row = actions_detail = 'display_lesson_type', 'hide_lesson_type',

    def display_lesson_type(self, request, pk):
        lesson_type = LessonTypes.objects.get(pk=pk)
        if lesson_type.display:
            messages.error(
                request, 'Тип игры уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontypes_changelist'), request)
        else:
            messages.success(
                request, 'Тип игры опубликован')
            lesson_type.display = True
            lesson_type.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontypes_changelist'), request)

    def hide_lesson_type(self, request, pk):
        lesson_type = LessonTypes.objects.get(pk=pk)
        if not lesson_type.display:
            messages.error(
                request, 'Тип игры уже спрятан')
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontypes_changelist'), request)
        else:
            messages.success(
                request, 'Тип игры спрятан')
            lesson_type.display = False
            lesson_type.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_lessontypes_changelist'), request)

    display_lesson_type.short_description = 'Опубликовать'
    display_lesson_type.url_path = 'publish-lesson-type'
    hide_lesson_type.short_description = 'Спрятать'
    hide_lesson_type.url_path = 'hide-lesson-type'


@admin.register(EducationProcesses)
class EducationProcessesAdmin(ActionsModelAdmin, DraggableMPTTAdmin):
    list_display = ('tree_actions', 'name', 'language', 'display')
    list_display_links = ('name',)
    filter_fields = ('language', 'display')
    search_fields = ('name',)
    list_filter = (
        ('parent', TreeRelatedFieldListFilter),
    )
    actions_row = actions_detail = 'display_education_process', 'hide_education_process',

    def display_education_process(self, request, pk):
        education_process = EducationProcesses.objects.get(pk=pk)
        if education_process.display:
            messages.error(
                request, 'Познавательный процесс уже отображается')
            return HttpResponseRedirect(reverse_lazy('admin:info_educationprocesses_changelist'), request)
        else:
            messages.success(
                request, 'Познавательный процесс опубликован')
            education_process.display = True
            education_process.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_educationprocesses_changelist'), request)

    def hide_education_process(self, request, pk):
        education_process = EducationProcesses.objects.get(pk=pk)
        if not education_process.display:
            messages.error(
                request, 'Познавательный процесс уже спрятан')
            return HttpResponseRedirect(reverse_lazy('admin:info_educationprocesses_changelist'), request)
        else:
            messages.success(
                request, 'Познавательный процесс спрятан')
            education_process.display = False
            education_process.save()
            return HttpResponseRedirect(reverse_lazy('admin:info_educationprocesses_changelist'), request)

    display_education_process.short_description = 'Опубликовать'
    display_education_process.url_path = 'publish-education-process'
    hide_education_process.short_description = 'Спрятать'
    hide_education_process.url_path = 'hide-education-process'
