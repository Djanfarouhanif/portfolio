from django.contrib import admin

# Register your models here.
from .models import Content, Project


admin.site.register(Content)
admin.site.register(Project)