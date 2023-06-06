from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic, View

from to_do_list.forms import TaskForm
from to_do_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    ordering = ["-is_completed", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:task-list")


class TaskCompleteView(View):
    @staticmethod
    def post(request, pk) -> HttpResponseRedirect:
        task = Task.objects.get(pk=pk)

        if not task.is_completed:
            task.is_completed = True
        else:
            task.is_completed = False

        task.save()

        return HttpResponseRedirect(
            reverse("to_do_list:task-list")
        )


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tag-list")
