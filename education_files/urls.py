from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload', views.files, name='files'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
