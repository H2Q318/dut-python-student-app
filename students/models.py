from django.db import models

# Create your models here.
class Student(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    address = models.TextField()
    age = models.IntegerField(default=20)
    gender = models.BooleanField()