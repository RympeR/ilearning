from rest_framework import serializers
from apps.info.serializers import (
    AttachmentGetSerializer
)
from .models import (
    Post
)


class PostGetSerializer(serializers.ModelSerializer):

    hosting_url = serializers.URLField(required=False)
    attachment = AttachmentGetSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'
