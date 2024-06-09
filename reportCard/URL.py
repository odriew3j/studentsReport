from django.urls import path
from studentReport import views


urlpatterns = [
    path("",views.students_list, name = "students_list"),
]