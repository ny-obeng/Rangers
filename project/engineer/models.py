from django.db import models


class TrainingApplications(models.Model):
    PROGRAM_CHOICES = [
        ("apprenticeship", "Apprenticeship"),
        ("short-course", "Short Course"),
        ("professional", "Professional Certification"),
    ]

    full_name = models.CharField(max_length=100, default='Eg: John Doe')
    email = models.EmailField(default='example@example.com')
    phone_number = models.CharField(max_length=20, default='0000000000')
    program = models.CharField(max_length=50, choices=PROGRAM_CHOICES, default='apprenticeship')
    enrollment_date = models.DateField(auto_now_add=True)
    motivation = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='Active')

    class Meta:
        ordering = ["-enrollment_date"]
        verbose_name = "Application Requests"

    def __str__(self):
        return f"Trainee {self.full_name} - Program {self.program}"


class ServiceRequests(models.Model):
    SERVICE_CHOICES = [
        ("installation", "AC Installation"),
        ("repairs", "Repairs & Troubleshooting"),
        ("maintenance", "Maintenance"),
        ("energy", "Energy Efficiency Solutions"),
    ]

    full_name = models.CharField(max_length=100, default='Eg: John Doe')
    email = models.EmailField(default='example@example.com')
    phone_number = models.CharField(max_length=20, default='0000000000')
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='installation')
    message = models.TextField(max_length=300, blank=True)
    date_of_booking = models.DateTimeField(auto_now_add=True)
    preferred_date = models.DateField(default='2025-12-31')  # You can update this to any default future date

    class Meta:
        ordering = ["-date_of_booking"]
        verbose_name = "Service Requests"

    def __str__(self):
        return f"{self.full_name} - {self.service_type}"
