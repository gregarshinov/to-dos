from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.manage_todos, name="list"),
    path('create', views.create_todo, name="create")
]
