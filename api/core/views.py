from rest_framework import viewsets
from .serializers import StudenCardRepotSerializer
from .models import StudenCardRepot

class StudenCardRepotViewSet(viewsets.ModelViewSet):
    serializer_class = StudenCardRepotSerializer
    queryset = StudenCardRepot.objects.all()