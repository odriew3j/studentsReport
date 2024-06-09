from django.shortcuts import render
from django.http import HttpResponse
from .models import studentReport


def students_list(request):
    StudentReport = studentReport.objects.all()
    # return render(request, "studentReport/list.html", {"studentReport":studentReport})
    return HttpResponse("Hello world!")

