from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_type', 'date', 'time', 'contact_number', 'user_notes']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super(AppointmentForm, self).__init__(*args, **kwargs)
        
        if self.user and self.user.is_administrator():
            self.fields['admin_notes'] = forms.CharField(widget=forms.Textarea, required=False)
        if self.instance and self.instance.pk:
            self.fields['admin_notes'].initial = self.instance.admin_notes

    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'admin_notes' in self.cleaned_data:
            instance.admin_notes = self.cleaned_data['admin_notes']
        if commit:
            instance.save()
        return instance