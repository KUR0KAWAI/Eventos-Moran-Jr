
# Funcion que convierte de tipos de datos de Python a JSON

from rest_framework import serializers
from .models import Eventos

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'