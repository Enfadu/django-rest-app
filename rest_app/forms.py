from django.forms import ModelForm
from django import forms
from rest_app.models import NameModel

class name_form(forms.ModelForm):
    class Meta():
        model = NameModel
        fields = ('name','email')
