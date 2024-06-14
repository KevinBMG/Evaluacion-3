from rest_framework import serializers
from libreriaApp.models import libro, autor

class autorSerializer(serializers.ModelSerializer):
    class Meta:
        model = autor
        fields = '__all__'

class libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = libro
        fields = '__all__'