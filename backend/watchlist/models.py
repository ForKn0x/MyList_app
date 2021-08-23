from django.db import models

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

    def __str__(self):
        return self.title
