from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList


def home(request):
    todos = ToDoList.objects.all()
    context = {"todo_list": todos}
    return render(request, 'base/home.html', context)


def item(request, pk):
    todo = ToDoList.objects.get(id=pk)

    context = {"item": todo}
    return render(request, "base/single.html", context)
