from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from .serializers import *
from .models import *

"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)



"""
API view for displaying tasks
"""
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

""" 
API view for displaying single task
"""

@api_view(['GET'])
def singleTaskList(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)


""" 
API Overview for updating a single task
"""

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = task , data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



""" 
API Overview for creating a new task
"""
@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response( serializer.data)    








# class TaskView(viewsets.ModelViewSet):
#     serializer_class = CreateTaskSerializer
#     queryset = Task.objects.all()   
#     permission_classes = [AllowAny]

#     # @method_decorator(csrf_exempt)
#     def post(self , request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception = True)

#         if valid:
#             status_code = status.HTTP_201_CREATED

#             response = {
#                 'status_code': status_code,
#                 'message': 'message created successfully',
#                 'createdTask': {
#                     'task_name' : serializer.data['task_name'],
#                      'task_description': serializer.data['task_description'],
#                       'created_by': serializer.data['created_by'],
#                        'owner' : serializer.data['owner']
#                 }
#             }

#             return Response( response , status = status_code )