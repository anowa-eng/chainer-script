from django.contrib import admin
from . import models

# Register your models here.
admin.site.register([
    models.ActionEvent,
    models.DialogEvent,
    models.SceneHeader,
    models.TransitionEvent
])
