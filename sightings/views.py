from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
# Create your views here.

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)


def every_squirrel(request, squirrel_id):
    return HttpResponse("You're looking at squirrel %s." % squirrel_id)




