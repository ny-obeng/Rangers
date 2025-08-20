from django.shortcuts import render
from .forms import ApprenticeshipForm, AppointmentForm

def apprenticeship_view(request):
    if request.method == 'POST':
        form = ApprenticeshipForm(request.POST)
        if form.is_valid():
            # Process form data (send to database team, email, etc.)
            return render(request, 'apprenticeship_success.html', {'form': form})
    else:
        form = ApprenticeshipForm()
    return render(request, 'apprenticeship_form.html', {'form': form})

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Process form data (send to database team, email, etc.)
            return render(request, 'appointment_success.html', {'form': form})
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

