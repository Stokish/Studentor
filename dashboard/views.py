from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin
from requests import post
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404


def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_mentor(user):
    return user.groups.filter(name='Mentors').exists()


@login_required
@user_passes_test(is_student)
def course_types(request):
    return render(request, 'dashboard/course-types.html')


@login_required
@user_passes_test(is_student)
def courses(request):
    return render(request, 'dashboard/courses.html')
