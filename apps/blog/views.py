from django.http import request
from rest_framework import generics, permissions
from .models import (
    Post
)
from .serializers import (
    PostGetSerializer
)
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser


class PostListRetrieveAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PostGetSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            if user.user_subscription.subscription_plan > 1:
                return Post.objects.all()
        return Post.objects.filter(accessory_level=1)
