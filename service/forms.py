from django import forms
from .models import EntriesTime



class EntriesForm(forms.ModelForm):
    class Meta:
        model = EntriesTime
        exclude = ('user', )






