from django.db import models
from django.contrib.auth.models import AbstractUser
from Model_TODO.models import Task

class MyUser(AbstractUser):
    nickname = models.TextField()
    tasks = models.ManyToManyField(Task)


























