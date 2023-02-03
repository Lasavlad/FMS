from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(Fleet)
admin.site.register(Trip)
admin.site.register(Supplier)
admin.site.register(Maintainance)
admin.site.register(TripCost)