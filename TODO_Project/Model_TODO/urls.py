from django.urls import path

from . import views

urlpatterns = [
    path("mylist_task/", views.viewTasks, name="mylist_task"),
    path("createTask/", views.createTask, name="createTask"),
]