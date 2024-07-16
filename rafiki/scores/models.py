from django.db import models
from student.models import Student

# Create your models here.
class Scores(models.Model):
    score = models.AutoField(primary_key=True)
    value = models.IntegerField()
    position = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='scores')
   
    
    
    def __str__(self):
        return self.position