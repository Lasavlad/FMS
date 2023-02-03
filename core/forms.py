from django import forms
from .models import Trip

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