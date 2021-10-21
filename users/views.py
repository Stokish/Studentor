from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserUpdateForm, ProfileUpdateForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import Group
from .decorators import allowed_users, unauthenticated_user
from .models import Profile


def index(request):
    return render(request, 'main/index.html')


def get_vacancy(request):
    return render(request, 'main/vacancy.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form.save will raise a signal to create user and profile
            user = form.save()
            # now profile and user are created but we need our role to be saved
            # therefore we need to access it and save from form
            user.profile.user_role = form.cleaned_data.get('roles')

            if user.profile.user_role == 'student':
                my_group = Group.objects.get(name='Students')
                my_group.user_set.add(user)
            else:
                my_group = Group.objects.get(name='Mentors')
                my_group.user_set.add(user)

            user.save()

            # messages.success(request, 'Account was created for ' + user)
            return redirect('signin')
    context = {'form': form}
    return render(request, 'account/register.html', context)


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('course-types')
        else:
            messages.info(request, 'Username or password incorrect')
    context = {}
    return render(request, 'account/login.html', context)


def logOut(request):
    logout(request)
    return redirect('signin')


login_required(login_url='login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
        p_form = ProfileUpdateForm(instance=request.user)

    if request.user.profile.user_role == 'student':
        if request.user.groups.filter(name='Mentors').exists():
            my_group_2 = Group.objects.get(name='Mentors')
            my_group_2.user_set.remove(request.user)
        my_group = Group.objects.get(name='Students')
        my_group.user_set.add(request.user)

    else:
        if request.user.groups.filter(name='Students').exists():
            my_group_2 = Group.objects.get(name='Students')
            my_group_2.user_set.remove(request.user)
        my_group = Group.objects.get(name='Mentors')
        my_group.user_set.add(request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    if request.user.groups.filter(name='Students').exists():
        return render(request, 'main/profile.html', context)
    else:
        return render(request, 'main/profile-mentor.html', context)


@login_required
def profiles(request, pk, *args, **kwargs):
    global is_follower
    prof = Profile.objects.get(pk=pk)
    user = prof.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
        p_form = ProfileUpdateForm(instance=request.user)
    """
    followers = profile.followers.all()
    number_of_followers = len(followers)
    for follower in followers:
        if follower == request.user:
            is_follower = True
            break
        else:
            is_follower = False
    """
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': prof,
        'user': user,
    }
    return render(request, 'main/userprofile.html', context)


def is_student(user):
    return user.groups.filter(name='Students').exists()


def is_mentor(user):
    return user.groups.filter(name='Mentors').exists()


@login_required
@user_passes_test(is_student)
def get_profile(request):
    return render(request, 'main/profile.html')


@login_required
@user_passes_test(is_mentor)
def get_mentor_profile(request):
    return render(request, 'main/profile-mentor.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'main/profileUpdate.html', context)


class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        followers = profile.followers.all()

        context = {
            'profile': profile,
            'followers': followers,
        }

        return render(request, 'main/followers_list.html', context)


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        pr = Profile.objects.get(pk=pk)
        pr.followers.add(request.user)
        return redirect('profilePlace', pk=pr.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        pr = Profile.objects.get(pk=pk)
        pr.followers.remove(request.user)

        return redirect('profile', pk=pr.pk)


def deleted(request):
    return render(request, 'main/delete.html')


def showthis(request):
    count = Profile.objects.all().count()
    context = {
        'count_users': count
    }
    print(count)
    return render(request, 'main/admin.html', context)
