from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
