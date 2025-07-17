from rest_framework import serializers
from .models import Category, Product, Certification, Contact

class CategorySerializer(serializers.ModelSerializer):
    parents = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parents', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def get_parents(self, obj):
        return [
            {
                "id": parent.id,
                "name": parent.name,
                "slug": parent.slug,
                "parents": None,
                "created_at": parent.created_at,
                "updated_at": parent.updated_at,
            }
            for parent in obj.parents.all()
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'image', 'gramm', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'image']
        read_only_fields = ['id']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'phone1', 'phone2', 'fax', 'email1', 'email2']
        read_only_fields = ['id']