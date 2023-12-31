from django.shortcuts import render, redirect, get_object_or_404
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
    user_uploads = UploadedContent.objects.filter(user=user)
    public_uploads = UploadedContent.objects.filter(privacy='public')
    form = UploadFileForm()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = user
            upload.save()
            return redirect('profile')

    return render(request, 'profile.html', {'user': user, 'user_uploads': user_uploads, 'public_uploads': public_uploads, 'form': form})

@login_required
def delete_upload(request, upload_id):
    upload = get_object_or_404(UploadedContent, pk=upload_id, user=request.user)

    if request.method == 'POST':
        upload.delete()

    return redirect('profile')

def feed(request):
    # Fetch all public content
    public_uploads = UploadedContent.objects.filter(privacy='public')

    return render(request, 'feed.html', {'public_uploads': public_uploads})