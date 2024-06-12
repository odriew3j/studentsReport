from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudenCardRepotViewSet

router = DefaultRouter()
router.register(r'recipes', StudenCardRepotViewSet)

urlpatterns = [
    path("", include(router.urls))
]