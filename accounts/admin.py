from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username')

    # if you want to add custom fileld to admin forms, use 'fieldsets' for change and 'add_fieldsets' for add user or creation user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'email',
            ),
        }),
    )
   