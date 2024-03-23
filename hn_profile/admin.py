from django.contrib import admin

# Register your models here.
from .models import Content, Project, User_mail


admin.site.register(Content)
admin.site.register(Project)
admin.site.register(User_mail)