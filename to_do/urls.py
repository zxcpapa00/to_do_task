from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tasks/<int:pk>', TaskViewSet)


urlpatterns = [
    path('', include(router.urls))
]



