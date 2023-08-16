from django.views.generic import CreateView 
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.views import View
from django.shortcuts import redirect
from .forms import *
from django.urls import reverse_lazy

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    template_name = 'todo.html'
    success_url = '/todo/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo.html"
    success_url = '/todo/'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    form_class = TaskForm
    model =Task
    template_name = 'update.html'
    success_url = '/todo/'
    

class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = '/todo/'

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = '/todo/'
    template_name ='delete.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)