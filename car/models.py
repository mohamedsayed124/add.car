from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=20)
    year = models.IntegerField()


    def __str__(self):
     return f'{self.name}- {self.year} - {self.id}'
    