from django import forms
from .models import Classrooms

class ClassroomForm(forms.ModelForm):
    grade = forms.ChoiceField(choices=[(i, str(i)) for i in range(7, 13)])
    subject = forms.CharField(max_length=100)
    students_nie = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter NIE")

    class Meta:
        model = Classrooms
        fields = ['grade', 'subject']
