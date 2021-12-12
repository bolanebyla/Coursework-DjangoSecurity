from django import forms
from . import models


class TestDataForm(forms.ModelForm):
    class Meta:
        model = models.TestData
        fields = ('text',)
