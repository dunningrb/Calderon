from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import RegistrationForm, EditProfileForm
from .models import Connection


class ChangePasswordView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/change_password.html'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('registration:view_profile')
        else:
            return redirect('registration:change_password')


class ConnectionsView(LoginRequiredMixin, TemplateView):

    def get(self, request, operation, pk):
        referenced_user = User.objects.get(pk=pk)
        current_user = request.user
        if operation == 'add':
            Connection.add_connection(current_user, referenced_user)
        elif operation == 'remove':
            Connection.remove_connection(current_user, referenced_user)
        return redirect('registration:view_profile')


class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/edit_profile.html'

    def get(self, request):
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('registration:view_profile')
        else:
            return redirect('registration:edit_profile')


class LoginView(TemplateView):
    def get(self, request):
        return redirect('/accounts/login')


class NetworkView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/network.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        connections = Connection.objects.get(current_user=request.user).users.all()
        args = {'nbar': 'network', 'users': users, 'connections': connections}
        return render(request, self.template_name, args)


class RegisterView(TemplateView):
    template_name = 'registration/registration_form.html'

    def get(self, request):
        form = RegistrationForm()
        args = {'form': form, 'nbar': 'register'}
        return render(request, self.template_name, args)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query:index')
        else:
            return redirect('registration:register')


class ResetPasswordView(TemplateView):

    def get(self, request):
        return redirect('/accounts/password_reset')


class ViewProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

    def get(self, request, pk=None):
        if pk is None:
            user = request.user
            connections = Connection.objects.get(current_user=user).users.all()
            args = {'user': user, 'requesting_user': user, 'connections': connections, 'nbar': 'profile'}
        else:
            user = User.objects.get(pk=pk)
            connections = Connection.objects.get(current_user=request.user).users.all()
            args = {'user': user, 'requesting_user': request.user, 'connections': connections, 'nbar': 'none'}
        return render(request, self.template_name, args)
