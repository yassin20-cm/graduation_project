from django import forms
from .models import Request
from .models import User


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_description', 'related_file','request_state']


class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_state']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'academic_year', 'email']
