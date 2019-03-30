from django.shortcuts import render
from . import models

# Create your views here.
def todo_list(request):
    return render(request, 'main.html')
