from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length= 100)
    story_line = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add= True)
    
    
    
    def __str__(self):
        return self.title
    
    