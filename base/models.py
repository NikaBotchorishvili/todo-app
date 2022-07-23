from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(null=True)
