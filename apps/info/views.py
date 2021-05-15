from rest_framework import generics, permissions

from .models import (
    TaskTypes,
    LearningRange,
    LearningSubjects,
    LessonTheme,
    LessonTypes,
    EducationProcesses,
    Attachment,
)
from .serializers import (
    TaskTypesGetSerializer,
    LearningRangeGetSerializer,
    LearningSubjectsGetSerializer,
    LessonThemeGetSerializer,
    LessonTypesGetSerializer,
    EducationProcessesGetSerializer,
    AttachmentGetSerializer,
)
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser


class TaskTypesListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = TaskTypes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TaskTypesGetSerializer


class LearningRangeListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = LearningRange.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LearningRangeGetSerializer


class LearningSubjectsListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = LearningSubjects.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LearningSubjectsGetSerializer


class LessonThemeListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = LessonTheme.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LessonThemeGetSerializer


class LessonTypesListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = LessonTypes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LessonTypesGetSerializer


class EducationProcessesListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = EducationProcesses.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = EducationProcessesGetSerializer


class AttachmentListAPI(generics.ListAPIView):
    permission_classes = permissions.AllowAny,
    queryset = Attachment.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = AttachmentGetSerializer
