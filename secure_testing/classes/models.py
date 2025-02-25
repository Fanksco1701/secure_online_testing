from django.conf import settings
from django.db import models
from accounts.models import Student  # Import the Student model from the accounts app

class Classrooms(models.Model):
    grade = models.CharField(max_length=2)
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Assuming the teacher is a user
    students = models.ManyToManyField(Student, blank=True)  # Add a Many-to-Many relationship with Student

    def __str__(self):
        return f"{self.grade} - {self.subject}"
