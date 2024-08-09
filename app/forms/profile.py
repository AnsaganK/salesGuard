from django import forms

from app.models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['patronymic', 'password', 'role']
