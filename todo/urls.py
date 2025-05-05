from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/toggle/', views.toggle_task_completion, name='toggle_task'),
    path('export/', views.export_tasks_csv, name='export_tasks_csv'),

]
# blah