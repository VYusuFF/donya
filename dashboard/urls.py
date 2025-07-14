from django.urls import path
from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    CertificationListAPIView,
    ContactListAPIView,
)

urlpatterns = [
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/products/<int:category_id>/', ProductListAPIView.as_view(), name='product-list'),
    path('api/certifications/', CertificationListAPIView.as_view(), name='certification-list'),
    path('api/contacts/', ContactListAPIView.as_view(), name='contact-list'),
]
