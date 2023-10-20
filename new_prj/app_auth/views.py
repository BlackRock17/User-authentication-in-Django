from django import forms
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works'


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(views.View):
    pass


class LogoutUserView(views.View):
    pass
