from django.urls import path

from apps.user.views import LoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = "register" ),
    path('login/', LoginView.as_view(), name = "login" ),
    path('logout/', LogoutView.as_view(), name = "logout" ),
]
