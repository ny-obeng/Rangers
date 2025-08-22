from rest_framework import serializers
from .models import ApprenticeshipApplication

class ApprenticeshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprenticeshipApplication
        fields = '__all__'
