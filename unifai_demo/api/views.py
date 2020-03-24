from rest_framework import viewsets
# from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

# from .serializers import UserSerializer, GroupSerializer
from .serializers import FileSerializer, JobSerializer
from .models import File, Job


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    # permission_classes = [permissions.IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [permissions.IsAuthenticated]
