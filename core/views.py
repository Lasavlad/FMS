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
    trucks = Truck.objects.filter(status='I').values('unique_identifier')
    trucks_list = list(trucks)

    if request.method == 'POST':
        form = CreateTrip(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            truck_id = data['truck']

            #change associated truck of a trip to active
            i = 0
            for i in range(len(trucks_list)):
                
                if truck_id.__eq__(trucks_list[i]['unique_identifier']):
                    truck_status = Truck.objects.get(unique_identifier=truck_id)
                    truck_status.status = 'A'
                    truck_status.save()
                i + 1

            form.save()
            return redirect('core:dashboard')
    else:
        form = CreateTrip()
    context = {
        'form':form
    }

    return render(request, 'core/create_trip.html', context)
# Create your views here.
