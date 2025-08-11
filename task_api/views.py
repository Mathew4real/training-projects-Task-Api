from django.shortcuts import render
from . models import Task
from . serializers import TaskSerializer
from rest_framework import mixins,generics



class TasksView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class TaskDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
