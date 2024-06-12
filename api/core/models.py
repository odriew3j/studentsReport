from django.db import models
# Create your models here.

class StudenCardRepot(models.Model):
    DIFFICULTY_LEVELS = (
        ('Noob', 'Noob'),
        ('Medium', 'Medium'),
        ('Pro', 'Pro'),
    )
    codeNumber = models.PositiveIntegerField()
    name = models.CharField(max_length=120)
    lastName = models.CharField(max_length=400)
    picture = models.FileField()
    level = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    further_details = models.TextField()

    def __str_(self):
        return "Recipe for {}".format(self.name)