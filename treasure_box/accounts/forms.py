from django import forms
from .models import UploadedContent

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedContent
        fields = ['title', 'file', 'privacy']