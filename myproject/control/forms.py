from django import forms
from .models import Request
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_description', 'related_file','request_state']


class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_state']


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'academic_year', 'profile_image']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    