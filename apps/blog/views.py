from django.http import request
from rest_framework import generics, permissions
from .models import (
    Post
)
from .serializers import (
    PostGetSerializer
)


class PostListRetrieveAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostGetSerializer

    def get_queryset(self):
        user = self.request.user
        if user:
            if user.user_subscription.first().subscription_plan > 1:
                return Post.objects.all()
        return Post.objects.filter(accessory_level=1)
