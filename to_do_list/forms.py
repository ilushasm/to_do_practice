from django import forms

from to_do_list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
