from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .form import createNewTask, createNewProject

# Create your views here.

def index(request):
    title = "Bienvenido a Django"
    return render(request, "index.html", {'title': title})

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = "Robert"
    return render(request, "about.html", {"username": username})

def project(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    return render(request, "projects.html", {"projects": projects, "tasks": tasks})

def task(request):
    #oneTask = get_object_or_404(Task, id = id)
    tasks = Task.objects.all()
    if (request.method == "POST"):
        Task.objects.update(done = True)
        return redirect("tareas")
    else:
        return render(request, "tasks.html", {"tasks": tasks})

def createTask(request):
    if (request.method == "POST"):
        Task.objects.create(name = request.POST['name'], description = request.POST['description'], project_id = request.POST['projectId'])
        return redirect("/task/")
    else:
        return render(request, "createTask.html", {"form": createNewTask()})
    
def createProject(request):
    if (request.method == "POST"):
        Project.objects.create(name = request.POST['name'])
        return redirect("/project/")
    else:
        return render(request, "createProject.html", {"form": createNewProject()})