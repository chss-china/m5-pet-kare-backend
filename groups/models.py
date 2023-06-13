from django.db import models


from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


