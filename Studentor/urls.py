from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('index/', TemplateView.as_view(template_name='index.html')),
                  path('users/', include('users.urls')),
                  path('questions/', include('questions.urls')),
                  path('account/', include('accounts.urls')),
                  path('documents/', include('education_files.urls')),
                  path('todo/', include('todo_task.urls')),
                  path('in/', TemplateView.as_view(template_name="index.html")),
                  path('accounts/', include('allauth.urls')),
                  path('logout', LogoutView.as_view()),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
