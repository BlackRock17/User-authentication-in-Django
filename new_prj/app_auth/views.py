from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.views import generic as views
from django.shortcuts import render


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = auth_forms.UserCreationForm


class LoginUserView(views.View):
    pass


class LogoutUserView(views.View):
    pass
