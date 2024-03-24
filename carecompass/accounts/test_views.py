from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AccountViewsTests(TestCase):

    def test_signup_view(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_login_view(self):
        User = get_user_model()
        User.objects.create_patient(email='user@user.com', password='testpass123')
        response = self.client.post(reverse('accounts:login'), {'username': 'user@user.com', 'password': 'testpass123'})
        self.assertRedirects(response, reverse('accounts:dashboard'))
        
    def test_logout_view(self):
        self.client.login(email='user@user.com', password='testpass123')
        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('accounts:login'))
