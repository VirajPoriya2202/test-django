from django.db import models

# Create your models here.
class tes(models.Model):
    test1 = models.CharField(max_length=30)
    test2 = models.CharField(max_length=30,null=True,blank=True)