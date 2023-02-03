from django.shortcuts import render
from .models import *
from .forms import CreateTrip

def index(request):
    return render(request, 'core/index.html')


def dashboard(request):
    
    return render(request, 'core/dashboard.html')

def create_trip(request):
    form = CreateTrip()
    context = {
        'form':form
    }
    return render(request, 'core/create_trip.html', context)
# Create your views here.
