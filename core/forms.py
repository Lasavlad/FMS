from django import forms
from models import Trip

class CreateTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['truck', 'supplier', 'origin', 'destination']