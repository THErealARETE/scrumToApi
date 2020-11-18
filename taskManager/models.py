from django.db import models

# Create your models here.

from accounts.models import User

class Task(models.Model):
    task_name = models.CharField(max_length = 40)
    task_id = models.IntegerFied(unique = True)
    task_description = models.CharField(max_length = 1500)
    created_by = models.CharField(max_length = 40)
    owner = models.CharField(max_length = 40)
    user = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        related_name = 'goal_owner'
    )