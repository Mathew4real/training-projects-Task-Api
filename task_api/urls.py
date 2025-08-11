from django.urls import path
from . import views

urlpatterns = [
    path("Tasks/",views.TasksView.as_view()),
    path("Task/<int:pk>/",views.TaskDetail.as_view()),
]
