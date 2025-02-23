from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Add the home URL
    path('signup/teacher/', views.teacher_signup, name='teacher_signup'),
    path('signup/student/', views.student_signup, name='student_signup'),
    path('login/teacher/', views.teacher_login, name='teacher_login'),
    path('login/student/', views.student_login, name='student_login'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/classes/', views.view_classes, name='view_classes'),
    path('teacher/create_class/', views.create_class, name='create_class'),
]
