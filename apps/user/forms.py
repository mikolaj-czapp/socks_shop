from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import MyUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('city', 'street', 'postal_code', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('city', 'street', 'postal_code')


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


