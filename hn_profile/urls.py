from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]