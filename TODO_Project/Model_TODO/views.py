from django.shortcuts import render

def viewTasks(request):
    request.user.tasks
    return render(request, "Model_TODO/index.html")

def createTask(request):
    return render(request, "Model_TODO/createTask.html")
