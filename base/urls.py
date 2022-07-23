from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>", views.item, name='single'),
    path("create/", views.create, name='create'),
    path("edit/<int:pk>", views.edit, name="edit"),

    path("login/", views.UserLogin, name="login_page"),
    path("register/", views.register, name="register"),
    path("logout/", views.UserLogout, name="logout"),

    path("profile/<int:pk>", views.profile, name="profile"),
]
