from django import forms
from .models import ToDoItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = "__all__"

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = "__all__"
