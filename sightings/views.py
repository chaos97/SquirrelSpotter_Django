import json
import pandas as pd
import numpy as np
from datetime import date,datetime
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



def color_age_pie(df):
    age_color = df.groupby(['age','pri_color'])['id'].count().reset_index()
    colors = list(df['pri_color'].unique())
    pie_data = list()
    for i in colors:
        temp = int(age_color.query(f'age=="adult" & pri_color=="{i}"')['id'].iloc[0])
        temp2 = int(age_color.query(f'age=="juvenile" & pri_color=="{i}"')['id'].iloc[0])
        dic = {
                'name':i,
                'y':temp,
                'z':temp2,
                }
        pie_data.append(dic)


    pie_chart = {
            'chart': {
                'type': 'variablepie'
            },
            'title': {
                'text': 'Primary Colors of Squirrels'
            },
            'tooltip': {
                'headerFormat': '',
                'pointFormat': '<span style="color:{point.color}">\u25CF</span> <b> {point.name}</b><br/>' +
                    'Adult: <b>{point.y}</b><br/>' +
                    'Juvenile: <b>{point.z}</b><br/>'
            },
            'series': [{
                'minPointSize': 10,
                'innerSize': '20%',
                'zMin': 0,
                'name': 'colors',
                'data': pie_data
            }]
        }

    return json.dumps(pie_chart)


def activity_age_column(df):
    activities = ['running','chasing','climbing',\
                  'eating','foraging','kuks','quaas',\
                  'moans','tail_flags','tail_twitches',\
                  'approaches','indifferent','runs_from']
    adult = list()
    juvenile = list()

    for i in activities:
        adult.append(len(df[(df['age']=='adult') & (df[i]==True)]))
        juvenile.append(len(df[(df['age']=='juvenile') & (df[i]==True)]))

    column_chart = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Activities of Adult or Juvenile Squirrels'
            },
            'xAxis': {
                'categories': [i.replace('_',' ').capitalize() for i in activities]
            },
            'yAxis': {
                'min': 0,
                'title': {
                    'text': 'Total Number of Each Activity'
                },
                'stackLabels': {
                    'enabled': True,
                    'style': {
                        'fontWeight': 'bold',
                        'color': "( // theme\
                            Highcharts.defaultOptions.title.style &&\
                            Highcharts.defaultOptions.title.style.color\
                        ) || 'gray'"
                    }
                }
            },
            'legend': {
                'align': 'left',
                'x': 60,
                'verticalAlign': 'top',
                'y': 0,
                'floating': True,
                'backgroundColor': "#ffffff",
                'borderColor': '#CCC',
                'borderWidth': 1,
                'shadow': False
            },
            'tooltip': {
                'headerFormat': '<b>{point.x}</b><br/>',
                'pointFormat': '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            'plotOptions': {
                'column': {
                    'stacking': 'normal',
                    'dataLabels': {
                        'enabled': True
                    }
                }
            },
            'series': [{
                'name': 'Adult',
                'data': adult
            }, {
                'name': 'Juvenile',
                'data': juvenile
            }]
        }

    return json.dumps(column_chart)

def heatmap(df):
    correlation = df[['running','chasing','climbing',\
                                  'eating','foraging','kuks','quaas',\
                                  'moans','tail_flags','tail_twitches',\
                                  'approaches','indifferent','runs_from']]
    correlation = correlation.corr()
    axis = [i.replace('_',' ').capitalize() for i in correlation.columns]
    data = list()

    for i in range(len(correlation)):
        for j in range(i,len(correlation)):
            temp = round(float(correlation.iloc[i,j]),2)
            data.append([i,j,temp])
            data.append([j,i,temp])


    return json.dumps(axis),json.dumps(data)


def date_age_line(df):
    date_age = df.groupby(['date','age'])['id'].count().reset_index()
    datelist = list(set(date_age['date']))
    datelist.sort()
    adult = list()
    juvenile = list()
    
    for i in datelist:
        temp = int(date_age[(date_age['date']==i) & (date_age['age']=='adult')]['id'].iloc[0])
        temp2 = int(date_age[(date_age['date']==i) & (date_age['age']=='juvenile')]['id'].iloc[0])
        adult.append(temp)
        juvenile.append(temp2)
        
    datelist = [date.strftime(i,"%Y-%m-%d") for i in datelist]
    line_chart = {
            'chart': {
                'type': 'line'
            },
            'title': {
                'text': 'Numbers of Squirrels as Time Goes'
            },
            'xAxis': {
                'categories': datelist
            },
            'yAxis': {
                'title': {
                    'text': 'Number of Squirrels'
                }
            },
            'plotOptions': {
                'line': {
                    'dataLabels': {
                        'enabled': True
                    },
                    'enableMouseTracking': False
                }
            },
            'series': [{
                'name': 'Adult',
                'data': adult
            }, {
                'name': 'Juvenile',
                'data': juvenile
            }]
        }
            
    return json.dumps(line_chart)
            


def stats(request):
    df = pd.DataFrame(Squirrel.objects.all().values())

    pie_chart = color_age_pie(df)
    column_chart = activity_age_column(df)
    axis,data = heatmap(df)
    line_chart = date_age_line(df)

    context = {
            'pie_chart': pie_chart,
            'column_chart': column_chart,
            'line_chart': line_chart,
            'axis': axis,
            'data': data,
            }

    return render(request,'sightings/stats.html',context)


