from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Certification, Contact
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CertificationSerializer,
    ContactSerializer
)


class CategoryListAPIView(APIView):
    def get(self, request):
        parent_ids = Category.objects.filter(parents__isnull=False).values_list('parents', flat=True).distinct()
        queryset = Category.objects.exclude(id__in=parent_ids)
        if not queryset.exists():
            return Response({'message': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListAPIView(APIView):
    def get(self, request, category_id):
        queryset = Product.objects.filter(category__id=category_id)
        if not queryset.exists():
            return Response({'message': 'No products found for this category id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CertificationListAPIView(APIView):
    def get(self, request):
        queryset = Certification.objects.all()
        if not queryset.exists():
            return Response({'message': 'No certifications found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CertificationSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CertificationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            certification = Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            return Response({'message': 'Certification not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CertificationSerializer(certification, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactListAPIView(APIView):
    def get(self, request):
        queryset = Contact.objects.all()
        if not queryset.exists():
            return Response({'message': 'No contacts found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
