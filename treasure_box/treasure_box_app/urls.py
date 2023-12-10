from django.urls import path
from .views import timeline, upload_file, shared_timeline

urlpatterns = [
    path('timeline/', timeline, name='timeline'),
    path('upload/', upload_file, name='upload'),
    path('shared-timeline/', shared_timeline, name='shared_timeline'),
    # Other URL patterns...
]