from rest_framework import viewsets
from .models import Button, MenuItem
from .serializers import ButtonSerializer, MenuItemSerializer

class ButtonViewSet(viewsets.ModelViewSet):
    queryset = Button.objects.all()
    serializer_class = ButtonSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer