from django.db import models

# Create your models here.
class Servies(models.Model):
    servies_icon=models.CharField(max_length=50)
    servies_title=models.CharField(max_length=50)
    servies_des = models.TextField()