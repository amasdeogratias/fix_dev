from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
        
# customer model
class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    customer_business = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:
        return self.customer_name
    
    
