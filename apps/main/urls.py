from django.urls import path

from apps.main import views

urlpatterns = [
    path('', views.index, name='home'),
    path("register/", views.register_request, name="register")
]