from django.db import models

# Create your models here.
class State(models.Model):
    statid=models.AutoField(primary_key=True)
    statename=models.CharField(max_length=255,default="",unique=True)