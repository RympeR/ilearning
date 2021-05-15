from django.urls import path
from .views import (
    TaskTypesListAPI,
    LearningRangeListAPI,
    LearningSubjectsListAPI,
    LessonThemeListAPI,
    LessonTypesListAPI,
    EducationProcessesListAPI,
    AttachmentListAPI,
)

urlpatterns = [
    path('task-types-list/', TaskTypesListAPI.as_view(), name='task-types-list'),
    path('learning-range-list/', LearningRangeListAPI.as_view(), name='learning-range-list'),
    path('learning-subjects-list/', LearningSubjectsListAPI.as_view(), name='learning-subjects-list'),
    path('lesson-theme-list/', LessonThemeListAPI.as_view(), name='lesson-theme-list'),
    path('lesson-type-list/', LessonTypesListAPI.as_view(), name='lesson-type-list'),
    path('education-process-list/', EducationProcessesListAPI.as_view(), name='education-process-list'),
    path('attachment-list/', AttachmentListAPI.as_view(), name='attachment-list'),    
]
