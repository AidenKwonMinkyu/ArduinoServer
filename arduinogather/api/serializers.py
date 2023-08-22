from rest_framework import serializers
from .models import *

class GatherItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatherItem
        fields = '__all__'