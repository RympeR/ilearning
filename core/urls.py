from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from core import settings
from .yazg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('info/', include('apps.info.urls')),
    path('user/', include('apps.users.urls')),
    path('blog/', include('apps.blog.urls')),
    path('lessons/', include('apps.lessons.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
