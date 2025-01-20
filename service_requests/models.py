from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Model to store customer information linked to a Django user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username} ({self.email})"


class ServiceRequest(models.Model):
    """Model to handle customer service requests."""
    SERVICE_TYPES = [
        ('Gas Leak', 'Gas Leak'),
        ('Maintenance', 'Maintenance'),
        ('Installation', 'Installation'),
        ('Billing Issue', 'Billing Issue'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Cancelled', 'Cancelled'),
    ]


    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="service_requests")
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending', choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.service_type} request by {self.customer.user.username} ({self.status})"


class RequestStatusUpdate(models.Model):
    """Model to track the history of status updates for a service request."""
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name="status_updates")
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.service_request} to '{self.status}' at {self.timestamp}"

from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15, unique=True)  
    password = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)  

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name 

