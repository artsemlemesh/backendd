from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ButtonViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'buttons', ButtonViewSet)
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]