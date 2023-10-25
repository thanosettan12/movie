from django.db import models


# Create your models here.
class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    disc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gal', default='default_image.jpg')
