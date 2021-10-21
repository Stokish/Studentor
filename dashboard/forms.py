import datetime

from .models import courseKeywords
from .models import courseDirection
from .models import courses
from django.forms import ModelForm, TextInput, Textarea, TimeInput, CharField
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


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
    date_lesson = forms.DateField(widget=DateInput)

    def clean_date_lesson(self):
        date = self.cleaned_data['date_lesson']
        if date < datetime.date.today():
            raise forms.ValidationError("Дата должна быть сегодня или в будущем!")
        return date

    class Meta:
        model = courses
        fields = ['subject',
                  'image',
                  'course_name',
                  'lesson_cost',
                  'description',
                  'date_lesson',
                  'start_time',
                  'end_time',
                  'duration',
                  'lesson_type',
                  'lesson_url', 'max_student']
        widgets = {
            "course_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            "description": Textarea(attrs={"rows": 5, "cols": 20,
                    'class': 'form-control',
                    'placeholder': 'Описания курса'
                }),
            "date_lesson": DateInput(),
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
            "max_student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Максимальное количество человек на курс'
            }),
            "lesson_cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена вашего курса'
            }),
        }
