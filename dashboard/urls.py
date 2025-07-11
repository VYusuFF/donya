from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductWeightViewSet, CertificationViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'weights', ProductWeightViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
