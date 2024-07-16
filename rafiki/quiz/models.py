from django.db import models
from course.models import Course

# Create your models here.
class Quiz(models.Model):
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,related_name='Quiz')
    description = models.TextField(blank=True)
    number_of_questions = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description