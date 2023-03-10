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
    unique_identifier = models.CharField(max_length=10)
    
    def __str__(self):
        return self.unique_identifier

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

    def __str__(self):
        return self.name

class Fleet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

class Driver(Staff):
   driver_id = models.IntegerField()



class Truck(Vehicle):
    STATUS_CHOICE = (
        ('A', 'Active'),
        ('I', 'Idle'),
        ('M', 'Maintainance'),
    )
    fleet = models.ForeignKey(
        Fleet, 
        on_delete = models.CASCADE
    )
    assigned_driver = models.OneToOneField(
        Driver,
        on_delete = models.CASCADE
    )
    load_capacity = models.IntegerField()
    axle_configuration = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='I')
    

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
    STATUS_CHOICE = (
        ('A', 'Arrived'),
        ('O', 'Ongoing'),
    )
    ROUTE_CHOICES = (
        ('K-L', 'kano - Lagos'),
        ('L-K', 'Lagos - Kano'),
    )
    truck = models.OneToOneField(
        Truck,
        on_delete = models.CASCADE,
        related_name='truck_trip',
        null=True,
        blank=True
    
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )
    route = models.CharField(max_length=3, choices=ROUTE_CHOICES)
    date_of_trip = models.DateField(null=True)
    time_of_departure = models.DateTimeField(null=True)
    diesel_required = models.IntegerField(blank=True, null=True)
    nature_of_load = models.CharField(max_length=64)
    load_weight = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')
    

    def __str__(self):
        return self.route

class CompletedTrips(models.Model):
    STATUS_CHOICE = (
        ('A', 'Arrived'),
        ('O', 'Ongoing'),
    )
    ROUTE_CHOICES = (
        ('K-L', 'kano - Lagos'),
        ('L-K', 'Lagos - Kano'),
    )
    truck_C = models.CharField(max_length=30)
    supplier_C = models.CharField(max_length=30)
    route_C = models.CharField(max_length=3, choices=ROUTE_CHOICES)
    date_of_trip_C = models.DateField(null=True)
    time_of_departure_C= models.DateTimeField(null=True)
    diesel_required_C = models.IntegerField(blank=True, null=True)
    nature_of_load_C = models.CharField(max_length=64)
    load_weight_C = models.IntegerField(blank=True, null=True)
    status_C = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')
    time_of_arrival_C = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.route_C



class TripCost(models.Model):
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name='trip_cost'
    )
    cost_of_diesel = models.IntegerField()
    revenue_settled = models.IntegerField()
    driver_upkeep = models.IntegerField()
    title = models.CharField(max_length=64)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cost = models.IntegerField(default=100)
    receipt = models.FileField(blank=True, null=True)
    
