# shop_management/models.py
from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name  # Return a meaningful representation for the admin interface

class Shop(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # Define choices for the type of business
    BUSINESS_TYPE_CHOICES = [
        ('grocery', 'Grocery Store'),
        ('clothing', 'Clothing Store'),
        ('electronics', 'Electronics Store'),
        ('restaurant', 'Restaurant'),
        ('other', 'Other'),
    ]
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE_CHOICES, default='other')
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.name  # Return a meaningful representation for the admin interface
