from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    description = models.TextField()