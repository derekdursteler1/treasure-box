from django import forms
from django.core.exceptions import ValidationError

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField(
        label='Upload File',
        help_text='Allowed file types: Image, Video, PDF, DOCX',
        validators=[
            # Define a custom validator for allowed file types
            lambda file: validate_file_extension(file, ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'pdf', 'docx'])
        ]
    )

def validate_file_extension(value, allowed_extensions):
    ext = value.name.split('.')[-1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed extensions are {", ".join(allowed_extensions)}')