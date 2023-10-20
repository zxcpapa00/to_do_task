from rest_framework import serializers

from to_do.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    deadline = serializers.DateTimeField()
    out_time = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'user', 'status', 'priority', 'worker', 'deadline', 'out_time']


class DetailTaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
