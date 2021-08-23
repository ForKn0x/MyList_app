from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=50)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='watchlist_platform')
    avgrating = models.FloatField(default=0.0)
    num_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.PositiveIntegerField(validators = [MinValueValidator(0) , MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    activ = models.BooleanField(default=True)
    watchlist = models.ForeignKey(Watchlist, on_delete= models.CASCADE, related_name='watchlist_reviews')

    def __str__(self):
        return str(self.review) + " On Movie " + self.watchlist.title 

