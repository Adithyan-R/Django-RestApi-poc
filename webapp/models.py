from django.db import models

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Product(models.Model):
    name = models.CharField(max_length=100)
    category=models.CharField(max_length=200)
    price=models.FloatField()
    image = models.ImageField(upload_to=nameFile,blank=True)



def __str__(self):
    return self.name