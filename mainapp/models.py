from django.db import models
from django.core import validators
# Create your models here.
from django.contrib.auth.models import User
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length= 100)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name= "watchlists")
    story_line = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add= True)
    avg_rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(5)])
    review_user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.CharField(max_length=300, null=True)
    watchlist= models.ForeignKey(WatchList, on_delete = models.CASCADE, related_name= "reviews")
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.watchlist.title +" - rate " + str(self.rating)
     