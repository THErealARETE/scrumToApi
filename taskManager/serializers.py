from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_id','task_name', 'task_description', 'created_by', 'owner']
