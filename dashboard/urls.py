from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CourseCreateView, CourseList, StudentCourseList, CourseUpdateView, CourseDeleteView, MentorCourseList

urlpatterns = [
                  path('directions/', views.CourseDirectionListView.as_view(), name='course-types'),
                  path('direction-<subject>/', CourseList.as_view(), name='courses'),
                  path('new-course/', CourseCreateView.as_view(), name='course-create'),
                  path('course/<int:pk>/update', CourseUpdateView.as_view(), name='cc-update'),
                  path('course/<int:pk>/delete', CourseDeleteView.as_view(), name='cc-delete'),
                  path('change-role', views.change_role, name='change-role'),
                  path('my/', StudentCourseList.as_view(), name='my-courses'),
                  path('my-created-course/', MentorCourseList.as_view(), name='my-created-courses'),
                  path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
                  path('course//<slug:key>/apply', views.ApplyCourseRedirectView.as_view(), name='course-apply'),
                  path('course/search/', views.SearchCourseListView.as_view(), name='course-search'),
                  path('direction/search/', views.SearchDirectionListView.as_view(), name='direction-search'),
                  path('mentor/search/', views.SearchMentorListView.as_view(), name='mentor-search')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
