from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_movies = models.ManyToManyField(Movie, blank=True, related_name='liked_by')

    def __str__(self):
        return self.user.username
