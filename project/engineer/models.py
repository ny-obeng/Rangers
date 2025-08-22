from django.db import models


class ApprenticeshipApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    cv_file = models.FileField(upload_to='apprenticeship_cvs/')
    message = models.TextField(blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

