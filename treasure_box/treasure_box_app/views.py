from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def timeline(request):
    return render(request, 'timeline.html')

def upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        # Process and save the file as needed
        # You can use Django forms or handle file processing here
        return redirect('timeline')  # Redirect back to the timeline after upload
    return redirect('timeline')  # Redirect in case of GET request or no file

# urls.py

    