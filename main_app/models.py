from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    attendence = models.IntegerField()

    def __str__(self):
        return self.name