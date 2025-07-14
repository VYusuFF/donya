from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, ProductWeight, Certification, Contact
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductWeightSerializer,
    CertificationSerializer,
    ContactSerializer
)

class CategoryListAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        if not queryset.exists():
            return Response({'message': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductListAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        if not queryset.exists():
            return Response({'message': 'No products found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductWeightListAPIView(APIView):
    def get(self, request):
        queryset = ProductWeight.objects.all()
        if not queryset.exists():
            return Response({'message': 'No product weights found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductWeightSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CertificationListAPIView(APIView):
    def get(self, request):
        queryset = Certification.objects.all()
        if not queryset.exists():
            return Response({'message': 'No certifications found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CertificationSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactListAPIView(APIView):
    def get(self, request):
        queryset = Contact.objects.all()
        if not queryset.exists():
            return Response({'message': 'No contacts found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
