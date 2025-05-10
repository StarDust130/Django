from django.db import models 
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    dated_added = models.DateField
