from django.shortcuts import render,redirect, get_object_or_404
from .models import Todo
from django.urls import path
from . import views



# to make a list

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('completed_task/<int:task_id>/', views.completed_task, name='completed_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('uncompleted_task/<int:task_id>/', views.uncompleted_task, name='uncompleted_task'),
    path('update_task/<int:task_id>', views.update_task, name='update_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    
]