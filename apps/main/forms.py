from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30)
    street = forms.CharField(max_length=30)
    postal_code = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("username", "email", "city", "street", "postal_code", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user