from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class Post(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='account', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    track = models.FileField(upload_to='music/')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.title}'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
   
    
    def tracks(self):
        if self.track:
            return 'http://127.0.0.1:8000' + self.track.url
        return ''