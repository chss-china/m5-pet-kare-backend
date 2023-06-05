from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(pre_delete, sender=Group)
def protect_group_deletion(sender, instance, **kwargs):
    if instance.pet_set.exists():
        raise Exception("Cannot delete a group with associated pets.")
