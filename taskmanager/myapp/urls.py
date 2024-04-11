from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('update/<int:task_id>/', views.update_task, name='update-task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task') # type: ignore
]