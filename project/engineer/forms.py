from django import forms
from .models import TrainingApplications, ServiceRequests

class TrainingApplicationForm(forms.ModelForm):
    class Meta:
        model = TrainingApplications
        fields = ['full_name', 'email', 'phone_number', 'program', 'motivation']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'program': forms.Select(attrs={
                'class': 'form-control',
            }),
            'motivation': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your motivation...',
                'rows': 4
            }),
        }




class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequests
        fields = ['full_name', 'email', 'phone_number', 'service_type', 'message', 'preferred_date']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Additional notes'
            }),
            'preferred_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
