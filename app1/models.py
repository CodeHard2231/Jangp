from django.db import models

# Create your models here.
class Feature(models.Model):
    # id : int
    # name : str
    # details : str
    name=models.CharField(max_length=50)
    #specifies max amt of chars thaT can be inside this characterfield
    details=models.CharField(max_length=300)
    
    