from django.contrib import admin
from .models import ToDoListItems, Profile, ToDoLists
# Register your models here.

admin.site.register(ToDoListItems)
admin.site.register(Profile)
admin.site.register(ToDoLists)
