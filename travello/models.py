from django.db import models

# Create your models here.

class Mini_pohled(models.Model):
    id : int
    img: str
    title : str
    title_low : str


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)