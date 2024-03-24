from django.test import TestCase
from .forms import AppointmentForm
from datetime import date, time

class AppointmentFormTests(TestCase):

    def test_form_valid(self):
        form_data = {
            'appointment_type': 'General Checkup',
            'date': date.today(),
            'time': time(10, 30),
            'contact_number': '1234567890',
            'user_notes': 'No allergies',
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_if_missing_fields(self):
        form_data = {}  # Simulating an empty form submission
        form = AppointmentForm(data=form_data)
        self.assertFalse(form.is_valid()) 
