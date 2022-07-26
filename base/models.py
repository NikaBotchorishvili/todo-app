from django.db import models
from django.contrib.auth.models import User

from config import settings


class ToDoLists(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist")
    name = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now=True)


class ToDoListItems(models.Model):

    list = models.ForeignKey(ToDoLists, on_delete=models.CASCADE, null=True, related_name="items")
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile", null=True)
    description = models.TextField(null=False, default="", blank=True)
    avatar = models.ImageField(null=True, default="avatar.png")
