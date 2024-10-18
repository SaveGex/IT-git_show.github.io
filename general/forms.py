from django import forms
from . import models
class Create(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ['name', 'link']
