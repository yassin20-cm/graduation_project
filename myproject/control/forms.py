from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_description', 'related_file','request_state']


class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_state']
