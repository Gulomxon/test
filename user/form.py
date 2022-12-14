from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accaunt
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):

    class Meta:
        model       = Accaunt
        fields      = ("username", "first_name", "last_name", "email", "password1", "password2")



class LoginAccauntForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Accaunt
        fields = ("username", "password")

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('login invalied')