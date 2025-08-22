from django.db import models


class TrainingApplications(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = ""
        ordering = ["-date_applied"]
        verbose_name = "Application Requests"

    def __str__(self):
        return self.full_name
    
class service_requests(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField(max_length=300, blank= True)
    date_of_booking = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = "service_requests"
        ordering = ["-date_of_booking"]
        verbose_name = " Service Requests"


    def __str__(self):
        return self.full_name

