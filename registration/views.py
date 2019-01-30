from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, EditProfileForm


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('registration:view_profile')
        else:
            return redirect('registration:change_password')
    elif request.method == "GET":
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('registration:view_profile')
        else:
            return redirect('registration:edit_profile')
    elif request.method == "GET":
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)


def login(request):
    args = {'nbar': 'login'}
    return redirect('/accounts/login', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args = {'nbar': 'register'}
        if form.is_valid():
            form.save()
            return redirect('query:index', args)
        else:
            return redirect('registration:register', args)
    elif request.method == "GET":
        form = RegistrationForm()
        args = {'form': form, 'nbar': 'register'}
        return render(request, 'registration/registration_form.html', args)


def reset_password(request):
    return redirect('/accounts/password_reset')


@login_required
def view_profile(request):
    args = {'user': request.user, 'nbar': 'profile'}
    return render(request, 'registration/profile.html', args)

