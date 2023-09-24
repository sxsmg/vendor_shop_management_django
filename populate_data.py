import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_shop_management.settings')
django.setup()

from shop_management.models import Vendor, Shop
from django.contrib.auth.models import User  # Import the User model

# Define dummy data for vendors and shops
vendors_data = [
    {
        'company_name': 'Vendor 1',
        'email': 'vendor1@example.com',
        'phone_number': '123-456-7890',
        'address': '123 Main St, City1',
        'user_data': {  # User data for Vendor 1
            'username': 'vendor1',  # Set a unique username
            'password': 'password123',  # Set a secure password
        },
    },
    {
        'company_name': 'Vendor 2',
        'email': 'vendor2@example.com',
        'phone_number': '456-789-0123',
        'address': '456 Elm St, City2',
        'user_data': {  # User data for Vendor 2
            'username': 'vendor2',  # Set a unique username
            'password': 'password456',  # Set a secure password
        },
    },
]

shops_data = [
    {
        'vendor_id': 1,  # Associate with Vendor 1
        'name': 'Shop A',
        'description': 'Shop A Description',
        'business_type': 'grocery',
        'latitude': 40.7128,
        'longitude': -74.0060,
    },
    {
        'vendor_id': 1,  # Associate with Vendor 1
        'name': 'Shop B',
        'description': 'Shop B Description',
        'business_type': 'clothing',
        'latitude': 34.0522,
        'longitude': -118.2437,
    },
    {
        'vendor_id': 2,  # Associate with Vendor 2
        'name': 'Shop C',
        'description': 'Shop C Description',
        'business_type': 'electronics',
        'latitude': 51.5074,
        'longitude': -0.1278,
    },
]

def populate_database():
    for vendor_data in vendors_data:
        # Create a User instance for the Vendor
        user_data = vendor_data.pop('user_data')
        user = User.objects.create(username=user_data['username'], password=user_data['password'])

        # Associate the User with the Vendor
        vendor_data['user'] = user

        # Create the Vendor instance
        vendor = Vendor.objects.create(**vendor_data)

        for shop_data in shops_data:
            if shop_data['vendor_id'] == vendor.id:
                # Associate the Shop with the Vendor
                Shop.objects.create(vendor=vendor, **shop_data)

if __name__ == '__main__':
    populate_database()
    print('Dummy data populated successfully.')
