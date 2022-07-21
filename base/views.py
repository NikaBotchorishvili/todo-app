from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList
from .forms import TodoListForm


def home(request):
    todos = ToDoList.objects.all()
    context = {"todo_list": todos}
    return render(request, 'base/home.html', context)


def item(request, pk):
    todo = ToDoList.objects.get(id=pk)

    context = {"item": todo}
    return render(request, "base/single.html", context)


def create(request):
    form = TodoListForm
    context = {"form": form}
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        ToDoList.objects.create(
            title=title,
            description=description
        )
        return redirect("home")
    return render(request, "base/create.html", context)


def edit(request, pk):
    listItem = ToDoList.objects.get(id=pk)
    form = TodoListForm(instance=listItem)

    context = {'form': form}
    if request.method == "POST":
        listItem.title = request.POST.get("title")
        listItem.description = request.POST.get("description")
        listItem.save()
        return redirect('home')
    return render(request, "base/edit.html", context)