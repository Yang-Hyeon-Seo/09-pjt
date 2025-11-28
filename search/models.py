from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField()
    link = models.CharField()
    description = models.TextField()