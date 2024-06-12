from django.shortcuts import render
from django.http import HttpResponse
from .models import studentReport
from .forms import StudentForm  # Import the form you'll need for adding a student

def students_list(request):
    student_report = studentReport.objects.all()
    return render(request, "studentReport/main_menu.html", {"student_report": student_report})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  # Create a form instance and populate it with the data from the request
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse('دانشجو با موفقیت اضافه شد!')
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})

def main(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == '1':
            return add_student(request)
        # elif choice == '2':
        #     # Add course logic
        # elif choice == '3':
        #     # Calculate student GPA logic
        # elif choice == '4':
        #     # Show student's courses logic
        # elif choice == '5':
        #     # Delete a course logic
        # elif choice == '6':
        #     # Delete all courses logic

    return render(request, "main_menu.html")