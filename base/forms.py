from django.forms import ModelForm, Textarea, TextInput
from .models import ToDoList


class TodoListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={
                "placeholder": 'Enter Todo item Title'
            }),

            'description': Textarea(attrs={
                'placeholder': "Enter A Description For Your task",
                "rows": 7,
                "cols": 30,
            }),

        }
