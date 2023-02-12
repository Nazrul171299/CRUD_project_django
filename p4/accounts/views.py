from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserCreateForm
class RegistrationView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "accounts/register.html"
    success_url = "/accounts/login"
