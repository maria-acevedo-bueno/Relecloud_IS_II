## APP (relecloud)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Default, go to index view
    path('about/', views.about, name='about'), #About page
    path('destinations/', views.destinations, name='destinations'), #Destinations page 
]