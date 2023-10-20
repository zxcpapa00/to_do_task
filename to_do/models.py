from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    COMPLETE = 'Завершена'
    INCOMPLETE = 'Не завершена'
    STATUSES = (
        (COMPLETE, 'Завершена'),
        (INCOMPLETE, 'Не завершена')
    )

    LOW = 'Низкий'
    MEDIUM = 'Средний'
    HIGH = 'Высокий'
    PRIORITIES = (
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий'),
    )

    name = models.CharField(max_length=128, unique=True)
    status = models.CharField(max_length=15, choices=STATUSES, default=INCOMPLETE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITIES, default=LOW)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
