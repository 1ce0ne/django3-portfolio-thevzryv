from django.shortcuts import render
from .models import Developer

def all_team(request):
    developers = Developer.objects.all()
    return render(request, 'team/all_team.html', {'developers': developers})