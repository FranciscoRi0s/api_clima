from rest_framework import serializers
from .models import Informacion

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Informacion
        fields=[
            'id',
            'temperatura',
            'humedad',
            'latitud',
            'longitud',
        ]