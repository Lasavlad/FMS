from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import CreateTrip, UpdateTrip, TripCostForm
import datetime


def index(request):
    return render(request, 'core/index.html')

#dashboard 
def dashboard(request):
    active_trips = Trip.objects.filter(status='O')
    completed_trips = CompletedTrips.objects.all()
    
    context = {
        'active_trips':active_trips,
        'completed_trips':completed_trips
    }
    return render(request, 'core/dashboard.html',context)


def update_trip(request, id):
    #truck = Truck.objects.filter(status='A')
    trip = Trip.objects.get(id=id)
    trip_id = trip.id
    
    status_form = UpdateTrip(request.POST or None, instance=trip)

    trip_cost_details = trip.trip_cost.all()

   
    if request.method == 'POST':
        if status_form.is_valid():
            data = status_form.cleaned_data
            
            if data['status'] == 'A':
                #GET TRUCK
                truck_id = trip.truck
                truck = Truck.objects.get(unique_identifier=truck_id)
                truck.status = 'I'


                #UPDATING COMPLETE FORM
                completed_trip = CompletedTrips(
                    truck_C = trip.truck.unique_identifier,
                    supplier_C = trip.supplier.name,
                    route_C = trip.route,
                    date_of_trip_C = trip.date_of_trip,
                    time_of_departure_C = trip.time_of_departure,
                    diesel_required_C = trip.diesel_required,
                    nature_of_load_C = trip.nature_of_load,
                    load_weight_C = trip.load_weight,
                    time_of_arrival_C = datetime.datetime.now(),
                    status_C = 'A'
                )
                completed_trip.save()
            status_form.save()
            if data['status'] == 'A':
            
                truck.save()
                Trip.objects.get(id=id).delete()
            return redirect('core:dashboard')
    
    
    context = {
        'status_form':status_form,
        'trip_cost_details': trip_cost_details,
        'trip_id':trip_id

    }

    return render(request, 'core/update_trip.html', context)
           
    

def create_trip(request):
    trucks = Truck.objects.filter(status='I').values('unique_identifier')
    trucks_list = list(trucks)

    if request.method == 'POST':
        #create trip
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
        form = CreateTrip(initial={'status':'O'})
       
        form.fields['status'].initial = 'Ongoing'

    context = {
        'form':form,
        
    }

    return render(request, 'core/create_trip.html', context)

def create_trip_cost(request):
    if request.method == 'POST':
        form = TripCostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:dashboard')
    form = TripCostForm()
    context = {
        'form':form
    }
    return render(request, 'core/create_trip_cost.html', context)


def update_trip_cost(request, id):

    trip_cost_details = TripCost.objects.get(id=id)
    trip_id = trip_cost_details.trip.id
    

    if request.method == 'POST':
        trip_cost_form = TripCostForm(request.POST or None, instance=trip_cost_details)
        if trip_cost_form.is_valid():
            trip_cost_form.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    trip_cost_form = TripCostForm(request.POST or None, instance=trip_cost_details)
   
    context = {
        'trip_cost_form':trip_cost_form,
        'trip_id':trip_id
    }
    return render(request, 'core/update_trip_cost.html', context)

#truck
def trucks_information_page(request):
    trucks = Truck.objects.all()
    context = {
        'trucks':trucks,
    }
    return render(request, 'core/truck_info/trucks.html', context)

def truck_detail_page(request, id):
    truck = Truck.objects.get(id=id)
    context = {
        'truck':truck
    }
    return render(request, 'core/truck_info/truck_detail_view.html', context)