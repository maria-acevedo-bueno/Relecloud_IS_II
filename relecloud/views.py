from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, 'relecloud/index.html')

def about(request):
    return render(request, 'relecloud/about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'relecloud/destinations.html', {'destinations': all_destinations})
