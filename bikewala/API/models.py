from django.db import models

# Create your models here.

class Bike(models.Model):

    title=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    cc=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=300)


    def __str__(self):
        return self.title
    


