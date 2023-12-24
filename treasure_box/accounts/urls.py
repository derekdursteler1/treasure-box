from django.urls import path
from .views import SignUpView, profile, feed, delete_upload
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('feed/', feed, name='feed'),
    path('delete/<int:upload_id>/', delete_upload, name='delete_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)