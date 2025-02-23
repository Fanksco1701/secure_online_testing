from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm, StudentSignUpForm
from django.contrib.auth import login

# Teacher sign up view
def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home after signup
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
            return redirect('home')  # Redirect to home after signup
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
