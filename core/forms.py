from django import forms

from .models import Trip, CompletedTrips, TripCost

class CreateTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'truck', 
            'supplier',
            'route',
            'date_of_trip', 
            'time_of_departure',
            'diesel_required',
            'nature_of_load',
            'load_weight',
            'status'
        ]

class Completed_trip_form(forms.ModelForm):
    class Meta:
        model = CompletedTrips
        fields = [
                'truck_C', 
                'supplier_C',
                'route_C',
                'date_of_trip_C', 
                'time_of_departure_C',
                'diesel_required_C',
                'nature_of_load_C',
                'load_weight_C',
                'status_C'
            ]


class UpdateTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'diesel_required',
            'status'
        ]



class TripCostForm(forms.ModelForm):
    class Meta:
        model = TripCost
        fields = [
            'trip', 
            'cost_of_diesel', 
            'revenue_settled', 
            'driver_upkeep', 
            'title', 
            'date', 
            'description', 
            'cost', 
            'receipt' 
        ]
