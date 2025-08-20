from django.urls import path
from . import views

urlpatterns = [
    path('apprenticeship/', views.apprenticeship_view, name='apprenticeship'),
    path('appointment/', views.appointment_view, name='appointment'),
]
