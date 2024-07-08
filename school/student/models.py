from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.Field(primary_key = True)
    first_name = models.CharField(max_length=100)
    second_name= models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)