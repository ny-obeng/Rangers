from django.shortcuts import render

from rest_framework import generics
from .models import ApprenticeshipApplication
from .serializer import ApprenticeshipApplicationSerializer

class ApprenticeshipApplicationCreateView(generics.CreateAPIView):
    queryset = ApprenticeshipApplication.objects.all()
    serializer_class = ApprenticeshipApplicationSerializer
