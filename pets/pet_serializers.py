from rest_framework import serializers
from .models import Pet
from groups.models import Group
from traits.models import Trait
#from .pet_serializers import PetSerializer
from traits.trait_serializers import TraitSerializer
from groups.group_serializers import GroupSerializer
from .models import Sex_choices
from .models import models
class Sex_choices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    NOT_INFORMED = "Not Informed"
class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    #sex = serializers.CharField(max_length=20, choices=Sex_choices.choices, default=Sex_choices.NOT_INFORMED)
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    #traits = serializers.ManyToManyField(Trait)
    