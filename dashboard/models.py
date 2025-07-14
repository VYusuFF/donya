from django.db import models
from django.core.validators import FileExtensionValidator
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify
from parler.utils.context import switch_language

# Create your models here.

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200)
    )
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='children', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            with switch_language(self, 'en'):
                self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200),
        description = models.TextField()
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    gramm = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Certification(models.Model):
    image = models.FileField(
        upload_to='certifications/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])],
        null=True,
    )
    document = models.FileField(
        upload_to='certifications/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'txt'])],
        null=True,
    )

    def __str__(self):
        return self.image.name.split('/')[-1]

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True, null=True)
    