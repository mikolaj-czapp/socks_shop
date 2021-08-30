from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import MyUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('city', 'street', 'postal_code', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('city', 'street', 'postal_code')