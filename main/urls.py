from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='main'),
                  path('celebrity', views.celebrity, name='celebrity'),
                  path('about', views.about, name='about'),
                  path('create', views.create, name='create'),
                  path('find_mentor', views.find_mentor, name='find_mentor'),
                  path('register', views.register, name='register'),
                  path('mentor', views.mentor, name='mentor'),
                  path('mentor_auth', views.mentor_auth, name='mentor_auth'),
                  path('course_reg', views.course_reg, name='course_reg'),
                  path('create_course', views.create_course, name='create_course')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
