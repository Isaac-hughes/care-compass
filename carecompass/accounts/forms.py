from django import forms
from .models import PatientUser

class PatientUserSignUpForm(forms.ModelForm):
    class Meta:
        model = PatientUser
        fields = ['first_name', 'last_name', 'email', 'gp_code', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
