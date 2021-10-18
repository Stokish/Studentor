from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.course_types, name='course-types'),
                  path('/1', views.courses, name='courses'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
