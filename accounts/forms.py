from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AdminUserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('email','username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields=('email','username',)
