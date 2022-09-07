from pyexpat import model
from django.forms import ModelForm
from main.models import Email
from django import forms

class EmailForm(forms.Form):
    
    class Meta():
        model=Email
        fields=['nome', 'email']

