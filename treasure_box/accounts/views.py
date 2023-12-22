from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UploadedContent
from .forms import UploadFileForm

class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to the login page upon successful registration

@login_required
def timeline(request):
    user = request.user
    uploads = UploadedContent.objects.filter(user=user)
    return render(request, 'timeline.html', {'uploads': uploads})

@login_required
def upload_file(request):
    if request.method == 'POST':
        # Handle file upload logic, associate the upload with the user
        # ...

        return redirect('timeline')  # Redirect to the timeline page

@login_required
def profile(request):
    user = request.user
    uploads = UploadedContent.objects.filter(user=user)
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = user
            upload.save()
            return redirect('profile')

    return render(request, 'profile.html', {'user': user, 'uploads': uploads, 'form': form})