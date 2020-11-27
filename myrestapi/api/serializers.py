
from rest_framework import serializers
from .models import Detective

class DetectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detective
        fields = ('id','name','location')
