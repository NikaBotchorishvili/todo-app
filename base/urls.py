from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>", views.item, name='single'),
    path("create/", views.create, name='create'),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("login/", views.login, name="login")
]
