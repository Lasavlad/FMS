from django.shortcuts import render, redirect
from .models import *
from .forms import CreateTrip


def index(request):
    return render(request, 'core/index.html')


def dashboard(request):
    active_trips = Trip.objects.filter(status='O')
    
    context = {
        'active_trips':active_trips
    }
    return render(request, 'core/dashboard.html',context)

def create_trip(request):
    if request.method == 'POST':
        form = CreateTrip(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:dashboard')
    else:
        form = CreateTrip()
    context = {
        'form':form
    }

    return render(request, 'core/create_trip.html', context)
# Create your views here.
