from django.db import models

# Create your models here.

class Image(models.Model):
	BROWSE = models.ImageField(upload_to="myimage")

class Student(models.Model):
    SNO = models.IntegerField()
    COURSE = models.CharField(max_length=50)
    SCHOOL = models.CharField(max_length=50)
    YEAR = models.IntegerField()
    PERCENTAGE = models.IntegerField()
   
 