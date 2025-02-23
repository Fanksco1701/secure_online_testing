from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher, Student

# Teacher registration form
class TeacherSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    institution = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'name', 'subject', 'institution')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        teacher = Teacher(user=user, name=self.cleaned_data['name'], subject=self.cleaned_data['subject'], institution=self.cleaned_data['institution'])
        teacher.save()
        return user

# Student registration form
class StudentSignUpForm(UserCreationForm):
    NIE = forms.CharField(max_length=20)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'NIE')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        student = Student(user=user, NIE=self.cleaned_data['NIE'])
        student.save()
        return user
