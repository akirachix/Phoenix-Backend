from django.db import models

# Create your models here.
class Course (models.Model):
    course_name= models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
    course_level= models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return f"{self.course_name}"