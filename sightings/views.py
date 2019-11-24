from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_squirrels(request):
    return HttpResponse("Later I will list all squirrel sightings with links to edit and add sightings!")
