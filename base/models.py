from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title

