from django.urls import path
from .views import PostListRetrieveAPI

urlpatterns = [
    path('posts/', PostListRetrieveAPI.as_view(), name='view-posts'),   
]
