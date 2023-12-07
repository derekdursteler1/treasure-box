from django.urls import path
from .views import timeline, upload

urlpatterns = [
    path('timeline/', timeline, name='timeline'),
    path('upload/', upload, name='upload'),
    # Other URL patterns...
]