from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .pet_serializers import PetSerializer
from groups.group_serializers import GroupSerializer
from traits.trait_serializers import TraitSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination



class PetListCreateView(APIView,PageNumberPagination):
 def get(self, request):
     queryset = Pet.objects.all()
     result_page = self.paginate_queryset(queryset,request)
     serializer_class = PetSerializer(instance=result_page, many=True)
     
     return self.get_paginated_response(serializer_class.data)
    
 def post(self, request):
    serializer = PetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    group_data = serializer.validated_data.pop("group")
    trait_data = serializer.validated_data.pop("traits")

    group_name = group_data["scientific_name"].lower()
    trait_names = [trait["name"].lower() for trait in trait_data]

    group, _ = Group.objects.get_or_create(scientific_name=group_name)

    traits = []
    for trait_name in trait_names:
        trait = Trait.objects.filter(name__iexact=trait_name).first()
        if not trait:
            trait = Trait.objects.create(name=trait_name)
        traits.append(trait)

    pet = Pet.objects.create(group=group, **serializer.validated_data)
    pet.traits.set(traits)

    serialized_pet = PetSerializer(instance=pet)
    return Response(data=serialized_pet.data, status=status.HTTP_201_CREATED)



      

   