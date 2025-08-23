from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # homepage
    path("services/", views.book_service, name="services"),  # booking form
    path("about/", views.about, name="about"),  # about us
    path("career/", views.apply_training, name="career"),  # training form
    path('booking/', views.booking_view, name = 'booking'),
]
