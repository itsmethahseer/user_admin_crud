from dataclasses import field
from importlib.metadata import files
from django import forms
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
# to make crud operations i created another forms with same data
class user_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']
