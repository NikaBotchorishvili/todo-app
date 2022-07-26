from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoListItems, Profile, ToDoLists
from .forms import TodoListItemsForm, LogInForm, RegisterForm, ToDoListForm, ProfileForm, ToDoListItems
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404

def home(request):
    todos = ToDoListItems.objects.all()
    context = {"todo_list": todos}
    return render(request, 'base/home.html', context)


def item(request, pk):
    todo = ToDoListItems.objects.get(id=pk)

    context = {"item": todo}
    return render(request, "base/single.html", context)


def createList(request):
    form = ToDoListForm
    context = {"form": form}
    if request.method == "POST":
        name = request.POST.get('name')
        ToDoLists.objects.create(
            owner=request.user,
            name=name
        )
        return redirect("home")
    return render(request, "base/create.html", context)


def edit(request, pk):
    listItem = ToDoListItems.objects.get(id=pk)
    form = TodoListItemsForm(instance=listItem)

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

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()

            user.save()
            login(request, user)
            prof = Profile
            prof.objects.create(
                user=user,
                description=""
            )

            return redirect("home")
        else:
            messages.error(request)
    return render(request, "base/singup.html", context)


def UserLogout(request):
    logout(request)
    return redirect('home')


def list(request, pk):
    # Parent List
    l = ToDoLists.objects.get(pk=pk)

    # Child items of a parent list
    listItems = l.items.all()

    context = {"p_list": l, "list": listItems, "list_id": pk}
    return render(request, "base/list.html", context)


def profile(request, pk):
    user = User.objects.get(pk=pk)
    user_profile = Profile.objects.get(user=user)
    todo_lists = user.todolist.all()
    # todo_list_items =
    context = {"profile": user_profile, "lists": todo_lists}

    return render(request, "base/profile.html", context)


def delete(request, pk):
    item = ToDoListItems.objects.get(id=pk)

    item.delete()

    return redirect('home')


def edit_profile(request, pk):
    user = Profile.objects.get(pk=pk)
    form = ProfileForm(instance=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect("/profile/" + str(pk))
    context = {"form": form}
    return render(request, "base/edit_profile.html", context)


def createListItem(request, pk):
    l = ToDoLists.objects.get(pk=pk)
    form = TodoListItemsForm

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        ToDoListItems.objects.create(
            list=l,
            title=title,
            description=description
        )

        return redirect('/list/' + str(pk))
    context = {"form": form}

    return render(request, "base/create_item.html", context)


