from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.http import JsonResponse
from .models import Appointment
from django.utils.dateparse import parse_datetime
import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# Route constants
BOOK_APPOINTMENT = 'appointments:book_appointment'
VIEW_APPOINTMENTS = 'appointments:view_appointments'

@login_required
def book_appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect(VIEW_APPOINTMENTS)  # Redirect to view appointments
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('date_time')
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

@login_required
def admin_view_appointments(request):
    if request.user.is_admin:
        appointments = Appointment.objects.all().order_by('date_time')
        return render(request, 'appointments/admin_view_appointments.html', {'appointments': appointments})
    else:
        return redirect('some_error_page')  # or handle permission denied

@login_required
def create_appointment(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        appointment_type = data.get('appointmentType')
        date_time_str = f"{data.get('appointmentDate')} {data.get('appointmentTime')}"
        # Ensure to handle the timezone conversion properly here
        date_time = parse_datetime(date_time_str)
        contact_number = data.get('contactNumber')
        user_notes = data.get('additionalInfo')
        
        # Assuming you're storing datetime in UTC and converting based on the user's timezone
        date_time = pytz.utc.localize(date_time)
        
        appointment = Appointment.objects.create(
            user=user,
            appointment_type=appointment_type,
            date_time=date_time,
            contact_number=contact_number,
            user_notes=user_notes
        )
        
        return JsonResponse({'status': 'success', 'appointment_id': appointment.id})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)  # Ensures ownerships
    if request.method == "POST":
        appointment.delete()
        return redirect(VIEW_APPOINTMENTS)
    else:
        # Prevent deletion if not POST request
        return redirect(VIEW_APPOINTMENTS)