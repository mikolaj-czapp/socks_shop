from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from apps.user.forms import CustomUserCreationForm, RegisterForm
from django.contrib.auth import views as auth_views


def dashboard(request):
    return render(request, "users/dashboard.html")


# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "register.html",
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    successful_url = "/"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = "/"

