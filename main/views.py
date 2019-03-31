from django.shortcuts import render, redirect, Http404
from django.http import JsonResponse
from . import models
from . import forms


# Create your views here.
def manage_todos(request):
    if request.method == "POST" and request.is_ajax():
        task_forms = forms.TaskFormset(data=request.POST, queryset=models.Task.objects.all())
        if task_forms.is_valid():
            task_forms.save()
            return JsonResponse({"message": "success"})
        else:
            return JsonResponse({"message": task_forms.errors})
    ordering = request.GET.get("ordering")
    field_name = request.GET.get("field_name")
    if ordering and field_name:
        ordering = "-" if ordering == "desc" else ""
        queryset = models.Task.objects.order_by(ordering + field_name).all()
    else:
        queryset = models.Task.objects.all()
    task_forms = forms.TaskFormset(queryset=queryset)
    input_form = forms.TaskForm(initial={"priority": 1})  # normal
    return render(request, 'main.html', {"task_forms": task_forms,
                                         "input_form": input_form})


def create_todo(request):
    if request.method == "POST":
        input_form = forms.TaskForm(data=request.POST)
        if input_form.is_valid():
            input_form.save()
            return redirect("main:list")
    return Http404()
