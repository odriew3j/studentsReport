from django import forms
from .models import studentReport
from django.shortcuts import render, redirect



# Define the form for adding a new student directly in the view
class StudentForm(forms.ModelForm):
    class Meta:
        model = studentReport
        fields = ['studentsFierstName', 'studentsLastName', 'studentsNumber']

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_menu')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})