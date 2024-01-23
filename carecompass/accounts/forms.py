from django import forms
from .models import Patient

class PatientSignUpForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'gp_code', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
