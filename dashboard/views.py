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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import KeywordForm
from .forms import DirectionForm
from .forms import CourseForm
from .models import courses


class CourseList(ListView):
    model = courses
    template_name = 'dashboard/courses.html'
    context_object_name = 'courses'


class CourseCreateView(LoginRequiredMixin, CreateView):
    form_class = CourseForm

    template_name = 'dashboard/createcourse.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course-types')


def course_types(request):
    return render(request, 'dashboard/course-types.html')


# def Course_list(request):
#     return render(request, 'dashboard/courses.html')
