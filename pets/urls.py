
from django.urls import path
from django.urls import path
from .views import PetListCreateView,PetDetailView


urlpatterns = [
    path('pets/', PetListCreateView.as_view(), name='pet-list-create'),
   
]
