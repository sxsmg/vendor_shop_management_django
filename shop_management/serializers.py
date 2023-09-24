# shop_management/serializers.py
from rest_framework import serializers
from .models import Vendor, Shop

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'  # You can specify fields explicitly if needed

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
