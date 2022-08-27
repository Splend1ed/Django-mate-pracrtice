from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from app.forms import CreateUpdateTaskForm
from app.models import Tag, Task


class MainPage(ListView):
    template_name = "index.html"
    queryset = Task.objects.all()
    paginate_by = 12

# ---------------------------------------------------------------------------------


class TagsListView(ListView):
    template_name = "tags-list.html"
    queryset = Tag.objects.all()


class TagCreateView(CreateView):
    template_name = "tag-form.html"
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tag-delete-confirm.html"
    success_url = reverse_lazy("app:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tag-form.html"
    success_url = reverse_lazy("app:tags-list")
    fields = "__all__"

# ---------------------------------------------------------------------------------


class TaskCreateView(CreateView):
    template_name = "task-form.html"
    model = Task
    form_class = CreateUpdateTaskForm
    success_url = reverse_lazy("app:index")


class TaskDeleteView(DeleteView):
    model = Task
    queryset = Task.objects.all()
    template_name = "task-delete-confirm-view.html"
    success_url = reverse_lazy("app:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateUpdateTaskForm
    template_name = "task-form.html"
    success_url = reverse_lazy("app:index")


def status_task_redirect(request, pk):
    task = Task.objects.get(id=pk)
    if task.status:
        task.status = False
    else:
        task.status = True
    task.save()
    return redirect("app:index")
# ---------------------------------------------------------------------------------
