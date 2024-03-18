from django.shortcuts import render

from .models import Content,Project

def index(request):
    all_profile = Content.objects.all()
    profile = all_profile.first()
    return render(request, 'index.html', {'profile':profile})

def project(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }
    return render(request, 'project.html', context)


def project_post(request):
    get_id = request.GET["project_id"]
    project = Project.objects.get(id=get_id)

    return render(request, 'post.html', {'project':project})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    profile = Content.objects.all().first()

    return render(request, 'about.html', {'profile':profile})