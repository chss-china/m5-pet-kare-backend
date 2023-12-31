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
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import DestroyAPIView



class PetListCreateView(APIView,PageNumberPagination):
    def get(self, request):
        trait_name = request.query_params.get("trait", None)

        if trait_name:
            traits = Trait.objects.filter(name__iexact=trait_name)
            pets = Pet.objects.filter(traits__in=traits)
        else:
            pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request)
        serializer = PetSerializer(instance=result_page, many=True)
        return self.get_paginated_response(serializer.data)
        
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



class PetDetailView(APIView):
    
    def get(self, request, pet_id):
      try:
          pet = Pet.objects.get(id=pet_id)
          serializer = PetSerializer(pet)
          return Response(serializer.data, status=status.HTTP_200_OK)
      except ObjectDoesNotExist:
          return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pet_id):
       
        pet = get_object_or_404(Pet, id=pet_id)
        serialized_pet = PetSerializer(pet,data=request.data,partial=True)
        serialized_pet.is_valid(raise_exception=True)
        group_data = serialized_pet.validated_data.pop("group",None)
        traits_data = serialized_pet.validated_data.pop("traits",None)

        
        
        if group_data:
            group_name = group_data["scientific_name"]
            group = Group.objects.filter(scientific_name__iexact=group_name).first()
            if not group:
                group = Group.objects.create(scientific_name=group_name)
            pet.group = group
            
            print(pet.group)
        
        if traits_data:
            
            array = []
            for trait in traits_data:
                
                objtraits = Trait.objects.filter(name__iexact=trait["name"]).first()
                if not objtraits:
                 objtraits = Trait.objects.create(**trait)
            
                pet.traits.add(objtraits)
        

        pet.name = serialized_pet.validated_data.get("name", pet.name)
        pet.age = serialized_pet.validated_data.get("age", pet.age)
        pet.weight = serialized_pet.validated_data.get("weight", pet.weight)
        pet.sex = serialized_pet.validated_data.get("sex", pet.sex)
        
        pet.save()
        
        serializer = PetSerializer(instance=pet)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, pet_id):
            try:
                pet = Pet.objects.get(id=pet_id)
                pet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
      