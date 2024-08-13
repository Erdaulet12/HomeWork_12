from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
	model = Task
	template_name = 'task_list.html'
	context_object_name = 'tasks'


class TaskDetailView(DetailView):
	model = Task
	template_name = 'task_detail.html'
	context_object_name = 'task'


class TaskCreateView(CreateView):
	model = Task
	template_name = 'task_form.html'
	fields = ['title', 'description', 'priority', 'due_date']
	success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'task_form.html'
	fields = ['title', 'description', 'priority', 'due_date', 'completed']
	success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
	model = Task
	template_name = 'task_confirm_delete.html'
	success_url = reverse_lazy('task_list')


class TaskCompleteView(View):
	def post(self, request, pk):
		task = get_object_or_404(Task, pk=pk)
		task.completed = True
		task.save()
		return redirect('task_list')


class TaskIncompleteView(View):
	def post(self, request, pk):
		task = get_object_or_404(Task, pk=pk)
		task.completed = False
		task.save()
		return redirect('task_list')


class TaskByPriorityView(ListView):
	model = Task
	template_name = 'task_list.html'
	context_object_name = 'tasks'

	def get_queryset(self):
		priority = self.kwargs['priority']
		return Task.objects.filter(priority=priority)


class TaskByDueDateView(ListView):
	model = Task
	template_name = 'task_list.html'
	context_object_name = 'tasks'

	def get_queryset(self):
		return Task.objects.order_by('due_date')
