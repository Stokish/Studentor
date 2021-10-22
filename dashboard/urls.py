from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


from .views import CourseCreateView, CourseList, StudentCourseList

urlpatterns = [
                  path('directions/', views.CourseDirectionListView.as_view(), name='course-types'),
                  path('direction-<subject>/', CourseList.as_view(), name='courses'),
                  path('new-course/', CourseCreateView.as_view(), name='course-create'),
                  path('change-role', views.change_role, name='change-role'),
                  path('my/', StudentCourseList.as_view(), name='my-courses'),
                  path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
                  path('course/<slug:key>/apply', views.ApplyCourseRedirectView.as_view(), name='course-apply'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
