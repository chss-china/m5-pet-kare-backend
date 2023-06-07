from django.db import models
from django.utils import timezone
class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pets = models.ManyToManyField('pets.Pet')
    created_at = models.DateTimeField(auto_now_add=True)
