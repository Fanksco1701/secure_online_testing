from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Student(models.Model):
    nie = models.CharField(max_length=20, unique=True)  # NIE is the unique student identifier
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.nie})"
    
class Classroom(models.Model):
    GRADE_CHOICES = [(i, str(i)) for i in range(7, 13)]

    grade = models.IntegerField(choices=GRADE_CHOICES)
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="classrooms", blank=True)

    def __str__(self):
        return f"{self.subject} - Grade {self.grade} (Teacher: {self.teacher.username})"