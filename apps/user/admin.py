from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ('email', 'city', 'street', 'postal_code', 'is_staff', 'is_active',)
    list_filter = ('email', 'city', 'street', 'postal_code', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'city', 'street', 'postal_code')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'city', 'street', 'postal_code', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'city', 'street', 'postal_code',)
    ordering = ('email', 'city', 'street', 'postal_code',)


admin.site.register(MyUser, CustomUserAdmin)
