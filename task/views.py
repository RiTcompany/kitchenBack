from rest_framework import generics

from task.serializers import *
# Create your views here.

class TaskListView(generics.ListAPIView):
    authentication_classes = []
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(user__username=username)
            return queryset
        else:
            return []
    
class TaskDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
