from django.urls import path
from registration import views

app_name = 'registration'

urlpatterns = [
    path('change-password/', views.change_password, name='change_password'),
    path('login/', views.login, name='login'),
    path('password/', views.change_password, name='change_password'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),
    path('register/', views.register, name='register'),
    path('reset-password/', views.reset_password, name='reset_password'),
]