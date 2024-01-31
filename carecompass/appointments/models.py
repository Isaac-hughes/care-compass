from django.db import models
from django.conf import settings
import pytz

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    date_time = models.DateTimeField()
    duration = models.DurationField() 
    timezone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, default='UTC')
    user_notes = models.TextField(blank=True, null=True)
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.user} on {self.date_time}"
