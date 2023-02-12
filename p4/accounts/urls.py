from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import RegistrationView
urlpatterns = [
    path('accounts/login/',LoginView.as_view(template_name="accounts/login.html")),
    path('accounts/logout/',LogoutView.as_view()),
    path('accounts/register/',RegistrationView.as_view())
]