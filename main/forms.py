from django import forms
from . import models


class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ("name", "priority")
        widgets = {"name": forms.TextInput({"class": "form-control", "placeholder": "I need to..."}),
                   "priority": forms.Select({"class": "form-control"})}


TaskFormset = forms.modelformset_factory(model=models.Task,
                                         form=TaskForm,
                                         extra=0,
                                         fields=TaskForm.Meta.fields,
                                         widgets={"name": forms.TextInput({"class": "form-control-plaintext"}),
                                                  "priority": forms.Select({"class": "form-control"})})
