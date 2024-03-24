from django.test import TestCase
from .forms import PatientSignUpForm

class PatientSignUpFormTests(TestCase):

    def test_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@doe.com',
            'gp_code': '12345',
            'password': 'password123',
            'confirm_password': 'password123',
        }
        form = PatientSignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_form_not_valid(self):
        form_data = {
            'first_name': '£££',
            'last_name': '////',
            'email': 'john@doe.com',
            'gp_code': '12345',
            'password': 'password123',
            'confirm_password': 'notMatchingPassword',
        }
        form = PatientSignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_passwords_match(self):
        form = PatientSignUpForm(data={
            'email': 'test@test.com',
            'password': 'testpass123',
            'confirm_password': 'differentpass',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('confirm_password', form.errors)
