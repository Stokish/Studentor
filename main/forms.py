from .models import Task
from .models import Mentor
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дисциплина вопроса'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вопрос'
            })

        }


class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ["name", "email", "telephone", "university", "discipline"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша имя и фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'
            }),
            "telephone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "university": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш университет'
            }),
            "discipline": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дисциплина, в котором нуждаетесь ментора'
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
