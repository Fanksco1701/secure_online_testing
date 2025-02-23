from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    email = models.EmailField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    NIE = models.CharField(max_length=20)
    email = models.EmailField()
