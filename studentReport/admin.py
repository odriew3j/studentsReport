from django.contrib import admin
from .models import studentReport

@admin.register(studentReport)
class studentReport(admin.ModelAdmin):
    list_display = ["studentsNumber", "studentsFierstName", "studentsLastName", "created"]