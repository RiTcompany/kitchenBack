

from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', max_length=24)
    class Meta:
        model = Task
        fields = ('id', 'article', 'status', 'create_at', 'update_at',)
        extra_fields = {
            'url': {'view_name': 'task-detail', 'lookup_field': 'pk'},
        }
        