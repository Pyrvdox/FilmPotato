from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=128, blank=False)
    desc = models.models.TextField(blank=False)
    date = models.DateField(default=True)
    imag = models.ImageField(upload_to="images/")
    duration = models.IntegerField()
    rate = models.FloatField()
    author = models.CharField(max_length= 64)