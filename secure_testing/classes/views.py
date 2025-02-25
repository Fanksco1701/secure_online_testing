from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClassroomForm  # Import the ClassroomForm from forms.py
from accounts.models import Student  # Import the Student model from the accounts app

@login_required
def create_class(request):
    # List to track valid students
    valid_students = []
    
    if request.method == "POST":
        # Create a new ClassroomForm instance for the classroom details
        form = ClassroomForm(request.POST)
        
        if form.is_valid():
            # Extract the comma-separated NIEs and process them
            students_nie = form.cleaned_data["students_nie"]
            nie_list = [nie.strip() for nie in students_nie.split(",")]  # Split and clean the NIEs
            
            # Validate each NIE and add valid students
            for nie in nie_list:
                student = Student.objects.filter(NIE=nie).first()  # Check if the NIE exists
                if student:
                    valid_students.append(student)  # Add the student to the valid list
                    messages.success(request, f"Student with NIE {nie} added successfully!")
                else:
                    messages.error(request, f"Student with NIE {nie} not found.")
            
            # Create the classroom only after validating all students
            classroom = form.save(commit=False)
            classroom.teacher = request.user  # Assign the logged-in teacher
            classroom.save()

            # Add all valid students to the classroom
            if valid_students:
                classroom.students.add(*valid_students)  # Add all valid students at once
                messages.success(request, "Classroom created successfully with students!")
            
            return redirect("create_class")  # Redirect to allow the teacher to input another set of NIEs

    else:
        form = ClassroomForm()

    return render(request, "classes/create_class.html", {"form": form})
