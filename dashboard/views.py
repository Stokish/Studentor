from abc import ABC

from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.db.models import Q
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
from django.contrib.auth.models import Group, User
from .forms import KeywordForm
from .forms import DirectionForm
from .forms import CourseForm
from .models import CourseDirection, Course
from datetime import datetime, timedelta


class DirectionList(ListView):
    model = CourseDirection
    template_name = 'dashboard/course-types.html'
    context_object_name = 'direction'


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


class MentorCourseList(ListView):
    model = Course
    template_name = 'dashboard/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        self.author = get_object_or_404(User, id=self.request.user.id)

        return Course.objects.filter(author=self.author.id)


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'dashboard/createcourse.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course-types')


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ABC):
    model = Course
    fields = ['image',
              'course_name',
              'lesson_cost',
              'description',
              'date_lesson',
              'start_time',
              'end_time',
              'duration',
              'lesson_url', 'max_student']
    template_name = 'dashboard/createcourse.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


class CourseDeleteView(DeleteView, UserPassesTestMixin):
    model = Course
    template_name = 'dashboard/confirm-delete.html'
    success_url = reverse_lazy('deleted')

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


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
        self.object.students.add(self.request.user)
        self.object.save()
        # this is code for email sending
        # msg = "Вы хотите записаться на курс " + self.object.course_name + " от " + self.object.author.username + "?\n"
        # msg += "Если да, то перейдите по ссылке: \n"
        # msg += "\t " + "http://127.0.0.1:8000%s" % reverse('course-apply', kwargs={'key': self.object.key}) + "\n"
        # msg += "Если вы передумали и не хотите записываться на данный курс, то проигнорируйте данное письмо"
        # send_mail(
        #     subject='Course Application Confirmation email',
        #     message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[self.request.user.email]
        # )
        # self.email_msg = "Мы отправили письмо на вашу почту! Перейдите по ссылке в письме, чтобы записаться на курс."
        self.email_msg = "Вы успешно записались на курс."
        return self.render_to_response(self.get_context_data())


# this is used for course link which will be send to email
class ApplyCourseRedirectView(RedirectView):
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


class SearchCourseListView(ListView):
    model = Course
    template_name = "dashboard/courses.html"
    context_object_name = 'courses'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchCourseListView, self).get_context_data(
            *args, **kwargs)
        query = self.request.GET.get('q')
        context['search'] = query
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        courses = Course.objects.filter(
            Q(course_name__icontains=query) | Q(description__icontains=query)
        )
        context = {
            'courses': 'courses',
            'search': query,
        }
        return courses


class SearchDirectionListView(ListView):
    model = Course
    template_name = "dashboard/course-direction.html"
    context_object_name = 'directions'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchDirectionListView, self).get_context_data(
            *args, **kwargs)
        query = self.request.GET.get('q')
        context['search'] = query
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        directions = CourseDirection.objects.filter(Q(name__icontains=query))
        return directions


def change_role(request):
    if request.user.groups.filter(name='Students').exists():
        my_group_2 = Group.objects.get(name='Students')
        my_group_2.user_set.remove(request.user)
    request.user.profile.user_role = 'mentor'
    my_group = Group.objects.get(name='Mentors')
    my_group.user_set.add(request.user)
    return redirect('course-types')
