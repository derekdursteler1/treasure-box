from django.urls import path
from .views import SignUpView, profile
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', profile, name='profile'),
]