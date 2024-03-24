from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Appointment
from datetime import date, time

class AppointmentModelTests(TestCase):

    def test_appointment_creation(self):
        user = get_user_model().objects.create_patient(email='testuser@mail.com', password='testpass')
        appointment = Appointment.objects.create(
            user=user,
            appointment_type='Telephone',
            date=date.today(),
            time=time(10, 30),
            contact_number='1234567890',
            user_notes='No allergies',
            admin_notes='Follow-up in 3 months'
        )
        self.assertEqual(appointment.user, user)
        self.assertEqual(appointment.appointment_type, 'Telephone')
        self.assertEqual(appointment.contact_number, '1234567890')
        self.assertTrue(Appointment.objects.exists())
