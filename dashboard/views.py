from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, RedirectView
)
from django.views.generic.edit import FormMixin
from requests import post
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import KeywordForm
from .forms import DirectionForm
from .forms import CourseForm
from .models import Course, CourseDirection
from django.contrib.auth.models import User


class CourseList(ListView):
    model = Course
    template_name = 'dashboard/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.subject = get_object_or_404(CourseDirection, name=self.kwargs['subject'])
        return Course.objects.filter(subject=self.subject)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['subject'] = self.subject
        return data


class StudentCourseList(ListView):
    model = Course
    template_name = 'dashboard/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.student = get_object_or_404(User, id=self.request.user.id)

        return Course.objects.filter(students__in=[self.student])


class CourseCreateView(LoginRequiredMixin, CreateView):
    form_class = CourseForm

    template_name = 'dashboard/createcourse.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course-types')


class CourseDetailView(DetailView):
    template_name = 'dashboard/course-detail.html'
    model = Course
    context_object_name = 'course'
    email_msg = ''

    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['email_msg'] = self.email_msg
        return data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        msg = "Вы хотите записаться на курс " + self.object.course_name + " от " + self.object.author.username + "?\n"
        msg += "Если да, то перейдите по ссылке: \n"
        msg += "\t " + "http://127.0.0.1:8000%s" % reverse('course-apply', kwargs={'key': self.object.key}) + "\n"
        msg += "Если вы передумали и не хотите записываться на данный курс, то проигнорируйте данное письмо"
        send_mail(
            subject='Course Application Confirmation email',
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.request.user.email]
        )
        self.email_msg = "Мы отправили письмо на вашу почту! Перейдите по ссылке в письме, чтобы записаться на курс."
        return self.render_to_response(self.get_context_data())

class ApplyCourseRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'course-detail'

    def get_redirect_url(self, *args, **kwargs):
        course = get_object_or_404(Course, key=kwargs['key'])
        course.students.add(self.request.user)
        course.save()
        return super().get_redirect_url(course.pk)


class CourseDirectionListView(ListView):
    model = CourseDirection
    template_name = 'dashboard/course-direction.html'
    context_object_name = "directions"


def course_types(request):
    return render(request, 'dashboard/course-direction.html')
