from django.db import models
from django.contrib.auth.models import User

class UploadedContent(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)
    shared = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
