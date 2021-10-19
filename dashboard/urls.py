from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseCreateView, CourseList

urlpatterns = [
                  path('', views.course_types, name='course-types'),
                  path('/1', CourseList.as_view(), name='courses'),
                  path('new-course', CourseCreateView.as_view(), name='course-create'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
