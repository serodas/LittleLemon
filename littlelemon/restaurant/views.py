from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer
from .models import Booking,Menu
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
