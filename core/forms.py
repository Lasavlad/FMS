from django import forms
from .models import Trip

class CreateTrip(forms.ModelForm):
    custom_supplier = forms.CharField(max_length=100)
    class Meta:
        model = Trip
        fields = [
            'truck', 
            'custom_supplier',
            'origin',  
            'destination', 
            'date_of_trip', 
            'time_of_departure',
            'diesel_required',
            'nature_of_load',
            'load_weight',
            'status'
        ]