from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CarsList(generics.ListCreateAPIView):
    queryset = CarsList.objects.all()
    serializer_class = CarsListSerializers
    permission_classes = (IsAuthenticated,)
