from django import forms
from .models import Task


class TaskFrom(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["title","descripcion", "important"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control","placeholder": "Write a title"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control","placeholder": "Write a descriptcion"}),
            "important": forms.CheckboxInput(attrs={"class": "form-check-input m-auto"}),
            }