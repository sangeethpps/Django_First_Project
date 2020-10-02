from django.contrib.auth.models import User
from django import forms
from basicapp import models


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ('port_folio_site', 'profile_picture')
