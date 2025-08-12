from django.urls import path
from . import views

urlpatterns = [
    path("tasks/",views.Tasks),
    path("tasks/<int:pk>/",views.TaskDetail)
]