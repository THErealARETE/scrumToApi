from django.db import models

# Create your models here.

from accounts.models import User

class TaskStatus(models.Model):
    status_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.status_name

class Task(models.Model):

    # def count():
        # no = Task.objects.count()
        # if no == None:
        #     return 1 



# {
#     "user_id": 1,
#     "task_id": 1,
#     "task_name": "testing",
#     "task_description":"testing testing testing",
#     "created_by": "pelumi",
#     "owner": "pelumi"
# }


        # else:
        #     return no + 1    
    task_name = models.CharField(max_length = 40)
    task_id = models.IntegerField( primary_key = True ,unique = True)
    task_description = models.CharField(max_length = 1500)
    created_by = models.CharField(max_length = 40)
    owner = models.CharField(max_length = 40)
    # user = models.ForeignKey(
    #     User,
    #     on_delete = models.PROTECT,
    #     related_name = 'goal_owner'
    # )
    # task_status = models.ForeignKey(
    #     TaskStatus,
    #     on_delete = models.SET_NULL,
    #     null  = True,
    #     related_name = 'status_of_task'
    # )

    def __str__(self):
        return self.created_by 

class TaskHistory(models.Model):
    moved_by = models.CharField(max_length = 30)
    created_by = models.CharField(max_length = 30)
    moved_from = models.CharField(max_length = 50)
    moved_to = models.CharField(max_length = 50)
    time_of_action = models.DateField()
    # tasks = models.ForeignKey(
    #     Task,
    #     on_delete = models.PROTECT
    # )
    def __str__(self):
        return self.created_by 