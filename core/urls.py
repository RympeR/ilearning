from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/info/', include('apps.info.urls')),
    path('api/user/', include('apps.users.urls')),
    path('api/blog/', include('apps.blog.urls')),
    path('api/lessons/', include('apps.lessons.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
