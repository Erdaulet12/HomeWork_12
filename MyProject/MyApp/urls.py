from django.urls import path, re_path
from .views import (
	TaskListView,
	TaskDetailView,
	TaskCreateView,
	TaskUpdateView,
	TaskDeleteView,
	TaskCompleteView,
	TaskIncompleteView,
	TaskByPriorityView,
	TaskByDueDateView,
)

urlpatterns = [
	path('', TaskListView.as_view(), name='task_list'),
	path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
	path('task/create/', TaskCreateView.as_view(), name='task_create'),
	path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
	path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
	path('task/<int:pk>/complete/', TaskCompleteView.as_view(), name='task_complete'),
	path('task/<int:pk>/incomplete/', TaskIncompleteView.as_view(), name='task_incomplete'),
	path('tasks/priority/', TaskByPriorityView.as_view(), name='task_by_priority'),
	path('tasks/due/', TaskByDueDateView.as_view(), name='task_by_due_date'),

	re_path(r'^tasks/priority/(?P<priority>\d+)/$', TaskByPriorityView.as_view(), name='task_by_priority_regex'),
	re_path(r'^task/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task_detail_regex'),
	re_path(r'^task/(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='task_edit_regex'),
	re_path(r'^task/(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='task_delete_regex'),
	re_path(r'^task/(?P<pk>\d+)/complete/$', TaskCompleteView.as_view(), name='task_complete_regex'),
]
