from .models import courseKeywords
from .models import courseDirection
from .models import courses
from django.forms import ModelForm, TextInput, Textarea, TimeInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class KeywordForm(ModelForm):
    class Meta:
        model = courseKeywords
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ключевое слово'
            })}


class DirectionForm(ModelForm):
    class Meta:
        model = courseDirection
        fields = ['name', 'keywords']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название направления'
            }),
            "keywords": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ключевые слова'
            })
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = courses
        fields = ['subject', 'image', 'course_name', 'description', 'start_time', 'end_time', 'duration', 'lesson_type',
                  'lesson_url', 'max_student', 'author', 'students']
        widgets = {
            "course_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описания курса'
            }),
            "start_time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': '00:00',
                'format': '%H:%M'
            }),
            "end_time": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': '00:00',
                'format': '%H:%M'
            }),
            "duration": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длительность'
            }),
            "lesson_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на урок'
            }),
        }
