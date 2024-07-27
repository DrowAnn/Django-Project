from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse("<h1>Index Page</h1>")

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse("<h2>About</h2>")

def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def task(request, id):
    oneTask = get_object_or_404(Task, id = id)
    return HttpResponse("Hello Task: %s" % oneTask.name)