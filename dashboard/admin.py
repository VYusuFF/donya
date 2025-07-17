from django.contrib import admin
from parler.forms import TranslatableModelForm
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
from .models import Category, Product, Certification, Contact
# Register your models here.

class CategoryAdminForm(TranslatableModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parents']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['parents'].queryset = Category.objects.exclude(pk=self.instance.pk)

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    form = CategoryAdminForm
    list_display = ('name', 'slug', 'get_parents', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parents',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('parents',)

    def get_parents(self, obj):
        return ", ".join([str(parent.name) for parent in obj.parents.all()])
    get_parents.short_description = 'Parents'

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'category', 'gramm', 'image_tag', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    readonly_fields = ('created_at', 'updated_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: contain;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')
    search_fields = ('id', 'image')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: contain;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'

@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('address', 'phone1', 'phone2', 'fax', 'email1', 'email2')
    search_fields = ('address', 'phone1', 'phone2', 'email1', 'email2')
    fieldsets = (
        (None, {
            'fields': ('address', 'phone1', 'phone2', 'fax', 'email1', 'email2')
        }),
    )