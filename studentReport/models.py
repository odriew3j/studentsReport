from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator


class studentReport(models.Model):
    studentsNumber = models.CharField(max_length=10)
    studentsFierstName = models.TextField()
    studentsLastName = models.TextField()
    lessonName = models.TextField()
    lessonScore = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
     )
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")

class meta:
    ordering = ["-pcreated"]

def __str__(self) -> str:
    return f"{self.studentsNumber} writed by {self.author}"

