from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields I want to store

    def __str__(self):
        return self.user.username
    
class UploadedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', default='default_filename.txt')  # Adjust the default value as needed
    privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='public')

    def __str__(self):
        return self.title