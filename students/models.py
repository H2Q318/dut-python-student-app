from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    name = models.TextField(max_length=256)
    
    def __str__(self):
        return f'{self.id} {self.name}'

class Student(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    address = models.TextField()
    age = models.IntegerField(default=20)
    gender = models.BooleanField(default=True)
    email = models.EmailField(blank=False, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False, null=True)
    
    def __str__(self):
        return f'{self.id} - {self.code} - {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
    
class Course(models.Model):
    name = models.TextField(max_length=256)
    limit = models.IntegerField(default=30)
    startDate = models. DateField()
    endDate = models.DateField()
    students = models. ManyToManyField(Student, blank=True, null=True)
    
    def _str_(self):
        return f"{self.name}({self.id})"