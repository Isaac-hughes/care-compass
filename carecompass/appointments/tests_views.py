from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Appointment
from datetime import date, time

class AppointmentViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_patient(email='user@user.com', password='testpass123')
        self.client.post(reverse('accounts:login'), {'username': 'user@user.com', 'password': 'testpass123'})
        self.appointment = Appointment.objects.create(
            user=self.user,
            appointment_type='Telephone',
            date=date.today(),
            time=time(10, 30),
            contact_number='1234567890',
            user_notes='Please be on time.'
        )

    def test_view_appointments(self):
        response = self.client.get(reverse('appointments:view_appointments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/view_appointments.html')
        self.assertContains(response, 'Telephone')
        self.assertContains(response, '1234567890')
        self.assertContains(response, 'Please be on time.')
