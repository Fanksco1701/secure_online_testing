from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Classroom, Student

class ClassroomForm(forms.ModelForm):
    grade = forms.ChoiceField(choices=[(i, str(i)) for i in range(7, 13)])
    subject = forms.CharField(max_length=100)
    students_nie = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter NIEs separated by commas")

    class Meta:
        model = Classroom
        fields = ['grade', 'subject']

@login_required
def create_class(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.teacher = request.user  # Assign the logged-in teacher
            classroom.save()

            # Validate students by NIE
            student_nies = request.POST.get("students_nie", "").split(",")
            valid_students = []
            for nie in student_nies:
                nie = nie.strip()
                if nie:
                    student = Student.objects.filter(nie=nie).first()
                    if student:
                        valid_students.append(student)
                    else:
                        messages.error(request, f"Student with NIE {nie} not found.")

            if valid_students:
                classroom.students.set(valid_students)
                messages.success(request, "Class created successfully!")
                return redirect("view_classes")  # Redirect to the class listing page
            else:
                classroom.delete()  # Remove class if no valid students
                messages.error(request, "No valid students were added.")
    else:
        form = ClassroomForm()

    return render(request, "classes/create_class.html", {"form": form})
