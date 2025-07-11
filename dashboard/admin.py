from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
from .models import Category, Product, ProductWeight, Certification, Contact
# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'category', 'image_tag')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: contain;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'

@admin.register(ProductWeight)
class ProductWeightAdmin(admin.ModelAdmin):
    list_display = ('product', 'gramm')
    search_fields = ('product__name',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'document')
    search_fields = ('image', 'document')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: contain;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone1', 'phone2', 'fax', 'email1', 'email2')
    search_fields = ('address', 'phone1', 'phone2', 'email1', 'email2')
    fieldsets = (
        (None, {
            'fields': ('address', 'phone1', 'phone2', 'fax', 'email1', 'email2')
        }),
    )