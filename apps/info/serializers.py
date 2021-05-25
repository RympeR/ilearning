from rest_framework import serializers
from apps.utils.customFields import RecursiveField
from .models import (
    TaskTypes,
    LearningRange,
    LearningSubjects,
    LessonTheme,
    LessonTypes,
    EducationProcesses,
    Attachment,
)


class TaskTypesGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTypes
        fields = '__all__'


class LearningRangeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningRange
        fields = '__all__'


class LearningSubjectsGetSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        required=False, queryset=EducationProcesses.objects.all(),)

    class Meta:
        model = LearningSubjects
        fields = '__all__'


class LessonThemeGetSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        required=False, queryset=EducationProcesses.objects.all(),)

    class Meta:
        model = LessonTheme
        fields = '__all__'


class LessonTypesGetSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        required=False, queryset=EducationProcesses.objects.all(),)

    class Meta:
        model = LessonTypes
        fields = '__all__'


class EducationProcessesGetSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        required=False, queryset=EducationProcesses.objects.all(),)

    class Meta:
        model = EducationProcesses
        fields = '__all__'


class AttachmentGetSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Attachment
        fields = '__all__'

    def get_file(self, attachemnt):
        request = self.context.get('request')
        if getattr(attachemnt.file, 'url'):
            file_url = attachemnt.file.url
            return request.build_absolute_uri(file_url)
        return None
