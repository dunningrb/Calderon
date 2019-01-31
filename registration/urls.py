from django.urls import path
from registration.views import (
    LoginView, ChangePasswordView, EditProfileView, NetworkView, RegisterView, ResetPasswordView, ViewProfileView
)

app_name = 'registration'

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('login/', LoginView.as_view(), name='login'),
    path('network/', NetworkView.as_view(), name='network'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/edit', EditProfileView.as_view(), name='edit_profile'),
    path('profile/', ViewProfileView.as_view(), name='view_profile'),
    path('profile/(<pk>)', ViewProfileView.as_view(), name='view_profile_with_primary_key'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]