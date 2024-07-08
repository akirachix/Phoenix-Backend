from django.db import models

from quiz.models import Quiz
from student.models import Student
from subject.models import Subject

class Score(models.Model):
    score_id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='scores')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='scores', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
