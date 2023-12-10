from django.shortcuts import render, redirect
from .forms import UploadFileForm
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def timeline(request):
    return render(request, 'timeline.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            file = form.cleaned_data['file']

            # Save the file to a specific directory
            fs = FileSystemStorage()
            fs.save(file.name, file)

            # Optionally, you can store the file information in a database model
            # Example: FileModel.objects.create(title=title, file_name=file.name)

            return redirect('timeline')  # Redirect to a success page or modify as needed
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)