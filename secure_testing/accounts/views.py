from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm, StudentSignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Teacher sign up view
def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('teacher_dashboard')  # Redirect to home after signup (replace with a valid URL)
    else:
        form = TeacherSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Student sign up view
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home after signup (replace with a valid URL)
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


# Teacher login view
def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_teacher:  # Ensure the user is a teacher
                login(request, user)
                return redirect('teacher_dashboard')  # Redirect to the home page or a dashboard
            else:
                form.add_error(None, 'You must be a teacher to log in here.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# Student login view
def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_student:  # Ensure the user is a student
                login(request, user)
                return redirect('home')  # Redirect to the home page or a dashboard
            else:
                form.add_error(None, 'You must be a student to log in here.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required  # Ensure the user is logged in
def teacher_dashboard(request):
    # You can later pass the actual classes and other relevant data here
    return render(request, 'accounts/teacher_dashboard.html')

def view_classes(request):
    # Logic for displaying classes will go here
    return render(request, 'accounts/view_classes.html')

