from django.db import models
from groups.models import Group
from traits.models import Trait
class Sex_choices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    NOT_INFORMED = "Not Informed"
class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=Sex_choices.choices, default=Sex_choices.NOT_INFORMED)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='pets')
    traits = models.ManyToManyField(Trait)


