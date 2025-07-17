from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify
from parler.utils.context import switch_language

# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-]{7,20}$',
    message='Enter a valid phone number (7–20 digits, optional +, space or dash).'
)

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200)
    )
    slug = models.SlugField(unique=True, blank=True)
    parents = models.ManyToManyField('self', symmetrical=False, related_name='children', blank=True)
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

    def __str__(self):
        return self.image.name.split('/')[-1]

class Contact(TranslatableModel):
    translations = TranslatedFields(
        address = models.CharField(max_length=255)
    )
    phone1 = models.CharField(max_length=20, validators=[phone_validator])
    phone2 = models.CharField(max_length=20, blank=True, null=True, validators=[phone_validator])
    fax = models.CharField(max_length=20, validators=[phone_validator])
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True, null=True)
    
    def clean(self):
        super().clean()
        if self.phone1 and self.phone2 and self.phone1 == self.phone2:
            raise ValidationError("Phone1 and Phone2 cannot be the same.")