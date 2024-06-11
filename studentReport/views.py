from django.shortcuts import render
from django.http import HttpResponse
from .models import studentReport
import os


def students_list(request):
    StudentReport = studentReport.objects.all()
    # template_path = 'studentReport/list.html'
    # context = {'studentReport': StudentReport}
    # return render(request, template_path, context)
    return render(request, "studentReport/list.html", {"StudentReport":StudentReport})