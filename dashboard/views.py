from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Product, ProductWeight, Certification, Contact
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductWeightSerializer,
    CertificationSerializer,
    ContactSerializer
)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductWeightViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductWeight.objects.all()
    serializer_class = ProductWeightSerializer

class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
