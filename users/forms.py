from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

USER_ROLES = (
    ('student', 'Student'),
    ('mentor', 'Mentor')
)



class CreateUserForm(UserCreationForm):
    roles = forms.ChoiceField(label="roles", widget=forms.RadioSelect, choices=USER_ROLES)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'roles', 'password1', 'password2')
        # fields = UserCreationForm.Meta.fields + 'user_role'

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-group',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Last name'
            }),

        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-group',
                'placeholder': 'Password'
            })
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form-group',
                'placeholder': 'Repeat the password'
            })


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'gender', 'date_of_birth', 'university', 'address', 'telephone', 'website',
                  'strong_at', 'hobbies', 'user_role']
