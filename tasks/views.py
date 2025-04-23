from django.shortcuts import render ,redirect

# Create your views here.

from .forms import TaskForm
from .models import Task

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView     
from django.views.generic import DetailView    
from django.views.generic import UpdateView 
from django.views.generic import DeleteView

from django.urls import reverse_lazy


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')