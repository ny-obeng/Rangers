from django.contrib import admin
from .models import TrainingApplications, ServiceRequests

@admin.register(TrainingApplications)
class TrainingApplicationsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'program', 'email', 'phone_number', 'enrollment_date', 'status')
    list_filter = ('status', 'program')
    search_fields = ('full_name', 'email', 'phone_number', 'motivation')

@admin.register(ServiceRequests)
class ServiceRequestsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service_type', 'email', 'phone_number', 'preferred_date', 'date_of_booking')
    list_filter = ('service_type', 'date_of_booking')
    search_fields = ('full_name', 'email', 'phone_number', 'message')
