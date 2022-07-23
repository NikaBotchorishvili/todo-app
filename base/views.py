from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList
from .forms import TodoListForm, LogInForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


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


def UserLogin(request):
    form = LogInForm
    context = {"form": form}

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "username with that email doesn't exist")

            user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "invalid password")
    return render(request, "base/login.html", context)


def register(request):
    form = RegisterForm
    context = {"form": form}

    return render(request, "base/singup.html", context)


def UserLogout(request):
    logout(request)
    return redirect('home')