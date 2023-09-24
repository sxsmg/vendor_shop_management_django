# shop_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListCreateView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('shops/', views.ShopListCreateView.as_view(), name='shop-list'),
    path('shops/<int:pk>/', views.ShopDetailView.as_view(), name='shop-detail'),
    path('register/', views.VendorRegistrationView.as_view(), name='vendor-registration'),
    path('login/', views.VendorLoginView.as_view(), name='vendor-login'),
]
