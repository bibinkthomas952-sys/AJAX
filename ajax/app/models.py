from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)