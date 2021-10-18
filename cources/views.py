from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import KeywordForm
from .forms import DirectionForm
from .forms import CourseForm
from .models import courses


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = courses
    fields = ['course_name', 'description', 'subject', 'image', 'start_time', 'end_time', 'duration', 'lesson_type',
              'lesson_url', 'max_student']
    template_name = 'courses.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course-types')
