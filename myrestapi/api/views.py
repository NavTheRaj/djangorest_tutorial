from rest_framework import viewsets
from .serializers import DetectiveSerializer
from .models import Detective

class DetectiveViewSet(viewsets.ModelViewSet):
    queryset = Detective.objects.all().order_by('name') #querying database for all records
    serializer_class = DetectiveSerializer # Specifying Serializer Class 
