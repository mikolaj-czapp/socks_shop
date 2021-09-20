from django.contrib.auth.forms import AuthenticationForm
from django.views import generic

from apps.user.forms import CustomUserCreationForm, RegisterForm
from django.contrib.auth import views as auth_views

# TODO
# def dashboard(request):
#     return render(request, "users/dashboard.html")


class LoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = "/"


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = "/"

