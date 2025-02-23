from django.db import models
from django.contrib.auth.models import AbstractUser, User

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Teacher' if self.is_teacher else 'Student'}"