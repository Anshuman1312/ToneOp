from django.db import models

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length=100)
    Create_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name    
    
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Enrollment = models.CharField(max_length=10,unique=True)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Create_at = models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)
    
    
    def  __str__(self):
        return self.Name