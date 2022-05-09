from django import forms
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget

from .models import EntriesTime

class EntriesForm(forms.ModelForm):
    # date_time =
    class Meta:
        model = EntriesTime
        exclude = ('user', 'barber')
        # widgets = {
        #     'date': AdminDateWidget(),
        #     'time': AdminTimeWidget(),
        # }
