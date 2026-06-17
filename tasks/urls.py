from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:task_id>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),
]