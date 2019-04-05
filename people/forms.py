from django import forms
from .models import NeighborHood,Profile

class NeighborHoodForm(forms.ModelForm):
    class Meta:
        model = NeighborHood
        exclude = ['user','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

