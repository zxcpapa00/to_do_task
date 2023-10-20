from django.db.models import F
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Task
from .serializers import TaskSerializer, DetailTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'priority', 'deadline']
    ordering_fields = ['deadline']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user).annotate(
            out_time=F('deadline') - timezone.now()
        )
        return queryset

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            self.serializer_class = DetailTaskSerializer
        else:
            self.serializer_class = TaskSerializer
        return super().retrieve(request, *args, **kwargs)
