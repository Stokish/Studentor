from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseCreateView, CourseList, DirectionList

urlpatterns = [
                  path('', DirectionList.as_view(), name='course-types'),
                  path('/1', CourseList.as_view(), name='courses'),
                  path('new-course', CourseCreateView.as_view(), name='course-create'),
                  path('change-role', views.change_role, name='change-role'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
