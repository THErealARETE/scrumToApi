from .views import TaskView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('tasks', TaskView)

router = routers.SimpleRouter()
router.register(r'tasks', TaskView())