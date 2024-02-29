from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=128, blank=False)
    desc = models.TextField(blank=False)
    date = models.DateField(default=True)
    image = models.ImageField(upload_to="images/")
    duration = models.IntegerField()
    rate = models.FloatField(default=0)
    author = models.CharField(max_length= 64)