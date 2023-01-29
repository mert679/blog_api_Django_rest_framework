from django.db import models

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()


    def __str__(self) -> str:
        return f"{self.title}"