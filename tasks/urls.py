from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/edit/<int:task_id>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),

    path('audit-log/', views.audit_log, name='audit_log'),
]