from django.contrib import admin
from .models import studens

@admin.register(studens)
class studensAdmin(admin.ModelAdmin):
    list_display = ["studensNumber", "studensFierstName", "studensLastName", "created"]