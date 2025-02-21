from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TextAnalysisViewSet

router = DefaultRouter()
router.register(r'analyses', TextAnalysisViewSet, basename='textanalysis')

urlpatterns = [
    path('', include(router.urls)),
]