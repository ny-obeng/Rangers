from django.urls import path
from .views import ApprenticeshipApplicationCreateView

urlpatterns = [
    path('apply/', ApprenticeshipApplicationCreateView.as_view(), name='apprenticeship-apply'),
]
