from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedContent

def timeline(request):
    return render(request, 'timeline.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']

            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Set user to the authenticated user
                uploaded_content = UploadedContent(title=title, file=file, user=request.user)
            else:
                # Set user to None for anonymous uploads
                uploaded_content = UploadedContent(title=title, file=file, user=None)

            uploaded_content.save()

            return redirect('timeline')  # Redirect to the 'timeline' view
    else:
        form = UploadFileForm()  # Create an empty form for rendering

    return render(request, 'upload.html', {'form': form})


def shared_timeline(request):
    shared_content = UploadedContent.objects.filter(shared=True).order_by('-timestamp')
    return render(request, 'feed.html', {'shared_content': shared_content})