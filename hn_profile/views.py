from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib  import messages
from .models import Content,Project, User_mail

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
    if request.method == 'POST':
        subject = "Message depuit mon portfolio"
        message = request.POST['message']
        sender_email = request.POST['email']
        recipient_list = [f'{sender_email}']

        try:
            send_mail(subject, message, sender_email, recipient_list)
            messages.info(request, 'message envoyer acec succes')
        except Execption as e:
            messages.error(request, 'message non envoyer{}'.format(str(e)))
        if User_mail.objects.filter(email=sender_email).exists():
            pass
        else:
            
            new_email = User_mail.objects.create(email=sender_email)
            new_email.save()

    return render(request, 'contact.html')

def about(request):
    profile = Content.objects.all().first()

    return render(request, 'about.html', {'profile':profile})