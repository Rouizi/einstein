from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from decouple import config

from core import views


urlpatterns = [
    path(config('ADMIN'), admin.site.urls),
    path('', views.index, name='index'),
    path('', include(('core.urls', 'core'), namespace='core'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
