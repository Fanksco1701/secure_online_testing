from django.urls import path
from . import views

urlpatterns = [
    path('signup/teacher/', views.teacher_signup, name='teacher_signup'),
    path('signup/student/', views.student_signup, name='student_signup'),
]
