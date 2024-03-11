from django.db import models
from django.conf import settings


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    appointment_type = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    contact_number = models.CharField(max_length=15)
    user_notes = models.TextField(blank=True)
    admin_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.user} on {self.date} at {self.time}"
