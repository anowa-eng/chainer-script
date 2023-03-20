from django.db import models

# Create your models here.
class SceneHeader(models.Model):
    ext_int = models.BooleanField()
    place_name = models.TextField()
    time_of_day = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
class ActionEvent(models.Model):
    action = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)
class DialogEvent(models.Model):
    character = models.TextField()
    parenthetical = models.TextField(null=True, blank=True)
    dialog = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)
class TransitionEvent(models.Model):
    transition = models.TextField()
    timestamp = models.DateTimeField(null=True, blank=True)
