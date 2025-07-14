from rest_framework import serializers
from .models import Category, Product, Certification, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'image', 'gramm', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'image', 'document']
        read_only_fields = ['id']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'phone1', 'phone2', 'fax', 'email1', 'email2']
        read_only_fields = ['id']