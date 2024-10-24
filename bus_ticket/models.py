from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('operator', 'Bus Operator'),
        ('driver', 'Bus Driver'),
        ('client', 'Client'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Ensure superuser permissions are handled correctly
    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'


class Vendor(models.Model):
    name = models.CharField(max_length=100)  # Bus company name
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'operator'},related_name='vendor_owned')  # The user who owns this bus company

    def __str__(self):
        return self.name


class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'driver'})  # One driver per CustomUser
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='drivers')  # A driver is assigned to one vendor

    def __str__(self):
        return self.user.username


class Bus(models.Model):
    name = models.CharField(max_length=100)  # Bus name or identifier
    plate_number = models.CharField(max_length=20, unique=True)  # Unique bus plate number
    capacity = models.PositiveIntegerField()  # Number of seats available in the bus
    operator = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='buses')  # Each bus belongs to one operator

    def __str__(self):
        return f"{self.name} ({self.plate_number})"



class Route(models.Model):
    start_location = models.CharField(max_length=100)  # Starting point of the route
    end_location = models.CharField(max_length=100)  # End point of the route
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price for the route

    def __str__(self):
        return f"{self.start_location} to {self.end_location}"


class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='schedules')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='schedules')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, related_name='schedules', null=True, blank=True)  # Allow nulls temporarily
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"Bus: {self.bus.name} | Driver: {self.driver.user.username if self.driver else 'No Driver'} | Route: {self.route.start_location} to {self.route.end_location} | Departure: {self.departure_time}"


class Ticket(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='tickets')  # Each ticket is for a specific schedule
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tickets', limit_choices_to={'role': 'client'})  # Ticket is purchased by a client
    seat_number = models.PositiveIntegerField()  # Seat number assigned to this ticket
    purchase_date = models.DateTimeField(auto_now_add=True)  # When the ticket was purchased

    def __str__(self):
        return f"Ticket for {self.client.username} | Seat: {self.seat_number} | Schedule: {self.schedule}"
