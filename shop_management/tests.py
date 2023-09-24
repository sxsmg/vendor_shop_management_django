# shop_management/tests/test_views.py
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from shop_management.models import Vendor, Shop

class ShopAPITestCase(TestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create some test vendors and shops (you can adjust this based on your data)
        self.vendor1 = Vendor.objects.create(user=self.user, company_name='Test Vendor 1', email='vendor1@example.com')
        self.shop1 = Shop.objects.create(vendor=self.vendor1, name='Shop 1', description='Shop 1 Description', business_type='grocery', latitude=40.7128, longitude=-74.0060)
    
    def test_list_shops(self):
        url = reverse('shop-list')  # Assuming you have defined a URL named 'shop-list'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if the correct number of shops is returned
    
    def test_create_shop(self):
        url = reverse('shop-list')  # Assuming you have defined a URL named 'shop-list'
        data = {
            'vendor': self.vendor1.id,
            'name': 'Shop 2',
            'description': 'Shop 2 Description',
            'business_type': 'clothing',
            'latitude': 34.0522,
            'longitude': -118.2437,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shop.objects.count(), 2)  # Check if the shop was created

    def test_vendor_registration(self):
        url = reverse('vendor-registration')  # Assuming you have defined a URL named 'vendor-registration'
        data = {
            'username': 'newvendor',
            'password': 'newpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access_token' in response.data)  # Check if the access token is returned
    
    def test_vendor_login(self):
        url = reverse('vendor-login')  # Assuming you have defined a URL named 'vendor-login'
        data = {
            'username': self.user.username,
            'password': 'password',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)  # Check if the access token is returned

    # Add more test cases for Vendor and Shop CRUD operations and other views as needed
