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
from django.contrib.auth.models import Group
from .forms import KeywordForm
from .forms import DirectionForm
from .forms import CourseForm
from .models import courses, courseDirection


class DirectionList(ListView):
    model = courseDirection
    template_name = 'dashboard/course-types.html'
    context_object_name = 'direction'


class CourseList(ListView):
    model = courses
    template_name = 'dashboard/courses.html'
    context_object_name = 'courses'

    # def get_queryset(self):
    #     self.subject = get_object_or_404(courseDirection, name=self.kwargs['subject'])
    #     return courses.objects.filter(subject=self.subject)


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = courses
    fields = ['course_name', 'description', 'subject', 'image', 'lesson_cost', 'date_lesson', 'start_time', 'end_time',
              'duration',
              'lesson_type',
              'lesson_url', 'max_student']
    template_name = 'dashboard/createcourse.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course-types')


def change_role(request):
    if request.user.groups.filter(name='Students').exists():
        my_group_2 = Group.objects.get(name='Students')
        my_group_2.user_set.remove(request.user)
    my_group = Group.objects.get(name='Mentors')
    my_group.user_set.add(request.user)
    return redirect('course-types')

# def Course_list(request):
#     return render(request, 'dashboard/courses.html')
