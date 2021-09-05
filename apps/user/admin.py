from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ('username', 'email', 'city', 'street', 'postal_code', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'city', 'street', 'postal_code', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'city', 'street', 'postal_code', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'city', 'street', 'postal_code', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'city', 'street', 'postal_code',)
    ordering = ('username', 'email', 'city', 'street', 'postal_code',)




admin.site.register(MyUser, CustomUserAdmin)
