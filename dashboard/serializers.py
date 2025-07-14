from rest_framework import serializers
from .models import Category, Product, ProductWeight, Certification, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  
        read_only_fields = ['id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'image', 'price']
        read_only_fields = ['id']

class ProductWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWeight
        fields = ['id', 'product', 'weight', 'unit', 'price']
        read_only_fields = ['id']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'title', 'image']
        read_only_fields = ['id']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'location', 'email', 'phone', 'instagram', 'facebook', 'telegram']
        read_only_fields = ['id']
