from django.forms import ModelForm
from .models import ToDoList


class TodoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']
