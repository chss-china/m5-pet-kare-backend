from rest_framework import serializers
from .models import Trait
class TraitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField(read_only=True)
    #pets = serializers.ManyToManyField('pets.Pet')