from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>", views.item, name='single'),
    path("create/", views.createList, name='create'),
    path("edit/<int:pk>", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("list/<int:pk>", views.list, name="list"),
    path("create-item/<int:pk>", views.createListItem, name='create-item'),

    path("login/", views.UserLogin, name="login_page"),
    path("register/", views.register, name="register"),
    path("logout/", views.UserLogout, name="logout"),

    path("profile/<int:pk>", views.profile, name="profile"),
    path("profile/edit/<int:pk>", views.edit_profile, name="edit_profile"),
]
