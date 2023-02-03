from django.shortcuts import render
from models import *

def index(request):
    return render(request, 'core/index.html')


def dashboard(request):
    
    return render(request, 'core/dashboard.html')
# Create your views here.
