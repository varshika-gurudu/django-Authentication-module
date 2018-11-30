from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import PasswordInput



class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget = PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #Address = forms.CharField(widget = forms.Textarea)
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user = User.objects.filter(email=email)
        if user.count():
            raise  ValidationError("Email already exists")
        return email

    class Meta:
        model = User
        fields = ['username','email','password1','password2',]
