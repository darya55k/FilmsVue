from django import forms
from .models import *

class CreateAuthoringSerializer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Authoring