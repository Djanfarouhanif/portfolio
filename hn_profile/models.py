from django.db import models
import uuid
# Create your models here.

class Content(models.Model):
    id = models.UUIDField(max_length=500, default=uuid.uuid4,primary_key=True)
    profile_img = models.URLField(null=True)
    bio = models.TextField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Project(models.Model):
    project_url = models.URLField(null=True)
    title = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
class User_mail(models.Model):
    email = models.EmailField()

    def __str_(self):
        return self.email
