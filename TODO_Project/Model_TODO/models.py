from django.db import models

class Task(models.Model):
    name_task = models.CharField()
    discription = models.CharField()
    date = models.DateField()
    time = models.TimeField()