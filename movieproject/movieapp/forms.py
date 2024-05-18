from django import forms
from .models import movie
#forms.py is used to update the table data

class MovieForm(forms.ModelForm):
    class Meta:
        model = movie #name of the model we want to edit
        fields = ['name', 'desc', 'year', 'img']# fields we want to edit in list format
