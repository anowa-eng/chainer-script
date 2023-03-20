from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
import json

# Create your views here.
def index(req):
    return render(req, 'index.html')

def create_SceneHeader(req):
    new_object = SceneHeader.objects.create(**req)
    data = SceneHeaderSerializer(new_object).data
    json = json.dumps(data)
    return JsonResponse(json)
def create_ActionEvent(req):
    new_object = ActionEvent.objects.create(**req)
    data = ActionEventSerializer(new_object).data
    json = json.dumps(data)
    return JsonResponse(json)
def create_DialogEvent(req):
    new_object = DialogEvent.objects.create(**req)
    data = DialogEventSerializer(new_object).data
    json = json.dumps(data)
    return JsonResponse(json)
def create_TransitionEvent(req):
    new_object = TransitionEvent.objects.create(**req)
    data = TransitionEventSerializer(new_object).data
    json = json.dumps(data)
    return JsonResponse(json)