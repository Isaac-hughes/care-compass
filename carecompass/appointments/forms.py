from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time', 'duration', 'timezone', 'user_notes']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duration': forms.NumberInput(),  # or DurationInput if you used DurationField
        }
