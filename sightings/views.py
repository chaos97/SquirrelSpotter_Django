from django.shortcuts import render, redirect 
from django.http import HttpResponse,HttpResponseRedirect
from .models import Squirrel
from django.forms import ModelForm
# Create your views here.

class SquirrelForm(ModelForm):
    class EverySquirrel:
        model=Squirrel
        fields=[
                "lon",
                "lat",
                "squirrel_id",
                "shift",
                "date",
                "age",
                "pri_color",
                "location",
                "specific_location",
                "running",
                "chasing",
                "climbing",
                "eating",
                "foraging",
                "other_activities",
                "kuks",
                "quaas",
                "moans",
                "tail_flags",
                "tail_twitches",
                "approaches",
                "indifferent",
                "runs_from"
                ]

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)

def create(request):
    form = SquirrelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_squirrels')
    return render(request,'sightings/add.html',{'add':form})





