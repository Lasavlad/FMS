from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number_1 = models.CharField(max_length=10)
    phone_number_2 = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=64)
    hiring_date = models.DateField()
    salary = models.PositiveIntegerField()
    is_staff = models.BooleanField()   

    def __str__(self):
        return self.first_name 

    class Meta:
        abstract = True

class Vehicle(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    date_of_production = models.DateField()
    vin_number = models.IntegerField()
    
    def __str__(self):
        return self.make

    class Meta:
        abstract = True

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    name_in_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_1 = models.IntegerField()
    phone_2 = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200)
    description = models.TextField()

class Fleet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

class Driver(Staff):
   driver_id = models.IntegerField()



class Truck(Vehicle):
    fleet = models.ForeignKey(
        Fleet, 
        models.CASCADE
    )
    assigned_driver = models.OneToOneField(
        Driver,
        models.CASCADE
    )
    load_capacity = models.IntegerField()
    axle_configuration = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

class Maintainance(models.Model):
    maintaince_code = models.IntegerField()
    truck = models.ForeignKey(
        Truck, 
        models.CASCADE
    )
    title = models.CharField(max_length=64)
    date = models.DateField()
    description = models.CharField(max_length=64)
    cost = models.IntegerField()
    receipt = models.FileField()

    def __str__(self):
        return self.title
    
        
class Trip(models.Model):
    truck = models.ForeignKey(
        Truck,
        models.CASCADE
    )
    supplier = models.ForeignKey(
        Supplier,
        models.CASCADE
    )
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    date_of_trip = models.DateField()
    time_of_departure = models.DateTimeField()
    time_of_arrival = models.TimeField(blank=True, null=True)
    diesel_required = models.IntegerField()
    nature_of_load = models.CharField(max_length=64)
    load_weight = models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination}"


class TripCost(models.Model):
    truck = models.ForeignKey(
        Truck,
        models.CASCADE
    )
    trip = models.ForeignKey(
        Trip,
        models.CASCADE
    )
    cost_of_diesel = models.IntegerField()
    revenue_settled = models.IntegerField()
    driver_upkeep = models.IntegerField()
    title = models.CharField(max_length=64)
    date = models.DateField()
    description = models.TextField()
    cost = models.IntegerField(default=100)
    receipt = models.FileField()
    
