from django.urls import path
from .views import timeline, upload_file

urlpatterns = [
    path('timeline/', timeline, name='timeline'),
    path('upload/', upload_file, name='upload'),
    # Other URL patterns...
]