from django.urls import path
from . import views

urlpatterns = [
        path('',views.all_squirrels),
        path('add/',views.add_record),
        path('<str:squirrel_id>/',views.squirrel_details),
        ]
