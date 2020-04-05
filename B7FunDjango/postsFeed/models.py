from django.db import models

# Create your models here.
class PostFeed(models.Model):
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title