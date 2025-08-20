from django import forms

class ApprenticeshipForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

class AppointmentForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    reason = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
    
    
