from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Squirrel
from .forms import SquirrelForm
# Create your views here.

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/all.html',context)


def squirrel_map(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/map.html',context)


def add_record(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            new_squirrel = form.save()
            return HttpResponseRedirect('/sightings/')

    else:
        form = SquirrelForm()

    return render(request,'sightings/add.html',{'form':form.as_p()})


def squirrel_details(request,squirrel_id):
    if request.method == 'POST' and 'delete' in request.POST:
        squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
        squirrel.delete()
        messages.success(request, 'Successfully Delete!')
        return HttpResponseRedirect('/sightings/')
    elif request.method == 'POST':
        squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
        form = SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Update!')
            return HttpResponseRedirect(f'/sightings/{squirrel_id}/')
    elif request.method == 'GET':
        squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
        form = SquirrelForm(instance=squirrel)
        context = {
                'form':form.as_p(),
                'squirrel':squirrel,
                }
        return render(request,'sightings/modify.html',context)
