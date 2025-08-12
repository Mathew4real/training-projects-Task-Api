from rest_framework import status
from rest_framework . decorators import api_view
from rest_framework .response import Response
from .models import Task
from . serializers import TaskSerializer


@api_view(["GET","POST"])
def Tasks(request):
    if request.method == "GET":
        tarefas = Task.objects.all()
        serializer = TaskSerializer(tarefas, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def TaskDetail(request,pk):
    try:
        tarefas = Task.objects.get(pk = pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TaskSerializer(tarefas)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = TaskSerializer(tarefas,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        tarefas.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    
