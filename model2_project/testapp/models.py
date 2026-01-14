from django.db import models

# Create your models here.
class Students(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=60)
    sage=models.IntegerField()