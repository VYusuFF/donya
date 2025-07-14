from django.urls import path
from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductWeightListAPIView,
    CertificationListAPIView,
    ContactListAPIView,
)

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/products/', ProductListAPIView.as_view(), name='product-list'),
    path('api/weights/', ProductWeightListAPIView.as_view(), name='weight-list'),
    path('api/certifications/', CertificationListAPIView.as_view(), name='certification-list'),
    path('api/contacts/', ContactListAPIView.as_view(), name='contact-list'),
]
