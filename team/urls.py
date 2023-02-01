from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [ 
    path('',views.all_team, name='all_team')
]