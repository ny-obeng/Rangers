from django.shortcuts import render, redirect
from .forms import ServiceRequestForm, TrainingApplicationForm


def home(request):
    return render(request, "engineer/home.html")


def book_service(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()  # saves directly to service_requests table
            return redirect('services')  # redirect after submission
    else:
        form = ServiceRequestForm()
    
    context = {
        'form': form
    }
    return render(request, "engineer/services.html", context)


def about(request):
    return render(request, "engineer/about_us.html")


def apply_training(request):
    if request.method == "POST":
        form = TrainingApplicationForm(request.POST)
        if form.is_valid():
            form.save()  # saves directly to enrollments table
            return redirect('career')  # redirect after submission
    else:
        form = TrainingApplicationForm()
    
    context = {
        'form': form
    }
    return render(request, "engineer/career.html", context)

def booking_view(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')  # Or wherever you want after booking
    else:
        form = ServiceRequestForm()
    return render(request, "engineer/booking.html", {'form': form})
