# from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
# from .views import TaskView


# # urlpatterns = [
# #     path('create/', TaskView.as_view() , name = 'create_task_view')
# # ]


from django.urls import path 
from . import views
from rest_framework_simplejwt import views as jwt_views

{
    "task_name": "testing",
    "task_description":"testing testing testing",
    "created_by": "pelumi",
    "owner": "pelumi"
}


urlpatterns = [
    path('', views.apiOverview, name = 'api-overview'),
    path('task-list/', views.taskList, name = 'task-list'),
    path('task-list/<str:pk>/', views.singleTaskList, name = 'single-task-list'),
    path('task-update/<str:pk>/', views.taskUpdate , name = 'update-task'),
    path('task-create', views.createTask , name = 'create-task'),

]