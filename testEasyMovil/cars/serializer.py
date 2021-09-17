from rest_framework import serializers
from .models import *

class NumeroSerializer(serializers.ModelSerializer):
    #persona = PersonaSerializers()
    class Meta:
        model = cars
        fields = '__all__'
