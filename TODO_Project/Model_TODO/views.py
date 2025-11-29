from django.shortcuts import render, redirect

from . import forms, models


def viewTasks(request):
    if request.method == "POST":
        id = request.POST.get("task_id")
        task = models.Task.objects.get(id=id)
        task.delete()
    data = {
        "tasks": request.user.tasks.all()
    }
    return render(request, "Model_TODO/index.html", data)

def createTask(request):
    if request.method == "POST":
        form = forms.CreateTask(data=request.POST)
        if form.is_valid():
            task = form.save()
            request.user.tasks.add(task)
            return redirect("mylist_task")
    form = forms.CreateTask()
    return render(request, "Model_TODO/createTask.html", {"form":form})
