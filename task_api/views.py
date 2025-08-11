from django.shortcuts import render
from . models import Task
from . serializers import TaskSerializer
from rest_framework import mixins,generics



class TasksView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self,reqeust):
        return self.list(reqeust)
    
