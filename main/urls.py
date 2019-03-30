from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.edit_todos, name="list"),
    path('create', views.create_task, name="create")
]
