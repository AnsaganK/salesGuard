from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'password']
