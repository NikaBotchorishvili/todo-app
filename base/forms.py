from django.forms import ModelForm, Textarea, TextInput, EmailInput, PasswordInput
from .models import ToDoList

from django.contrib.auth.models import User


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


class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', "password"]
        widgets = {
            'email': EmailInput(attrs={
                "placeholder": "Enter Your Email"
            }),
            'password': PasswordInput(attrs={
                "placeholder": "Enter Your Password"
            }),
        }


