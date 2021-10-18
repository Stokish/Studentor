from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import CourseCreateView

urlpatterns = [
                  path('new-course', CourseCreateView.as_view(), name='course-create'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
