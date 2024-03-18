from django.db import models
import uuid
# Create your models here.

class Content(models.Model):
    id = models.UUIDField(max_length=500, default=uuid.uuid4,primary_key=True)
    profile_img = models.ImageField()
    bio = models.TextField()
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
