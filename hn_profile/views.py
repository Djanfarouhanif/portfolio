from django.shortcuts import render

from .models import Content

def index(request):
    all_profile = Content.objects.all()
    profile = all_profile.first()
    return render(request, 'index.html', {'profile':profile})

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')