from rest_framework import serializers
from .models import Actor

class ActorSerializer(serializers.ModelSeirializer):

    class Meta:
        model = Actor
        fields= '__all__'