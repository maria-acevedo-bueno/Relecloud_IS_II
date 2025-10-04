from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'relecloud/index.html')

def about(request):
    return render(request, 'relecloud/about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'relecloud/destinations.html', {'destinations': all_destinations})

class DestinationDetailView(generic.DetailView):
    template_name = 'relecloud/destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class DestinationCreateView(generic.CreateView):
    model = models.Destination
    template_name = 'relecloud/destination_form.html'
    fields = ['name', 'description']

class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    template_name = 'relecloud/destination_form.html'
    fields = ['name', 'description']

class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = 'relecloud/destination_confirm_delete.html'
    success_url = reverse_lazy('destinations')

class CruiseDetailView(generic.DetailView):
    template_name = 'relecloud/cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'