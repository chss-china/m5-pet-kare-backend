from rest_framework import serializers
from .models import Pet
from groups.models import Group
from traits.models import Trait

from traits.trait_serializers import TraitSerializer
from groups.group_serializers import GroupSerializer

from .models import models, Sex_choices

print(Sex_choices)
class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices= Sex_choices.choices, default=Sex_choices.NOT_INFORMED)
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    
    