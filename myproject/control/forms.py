from django import forms
from .models import Request
from .models import User

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_description']


class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_state']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'academic_year', 'email', 'phone_number', 'password']


class UserLoginForm(forms.Form):
    user_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control'}),
    )