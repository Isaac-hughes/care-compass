from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.http import JsonResponse
from .models import Appointment
from django.utils.dateparse import parse_date, parse_time
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
            return redirect(VIEW_APPOINTMENTS) 
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('date')
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

@login_required
def admin_view_appointments(request):
    if request.user.is_admin:
        appointments = Appointment.objects.all().order_by('date')
        return render(request, 'appointments/admin_view_appointments.html', {'appointments': appointments})
    else:
        return redirect('some_error_page')  

@login_required
def create_appointment(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user
        appointment_type = data.get('appointmentType')
        appointment_date = parse_date(data.get('appointmentDate'))
        appointment_time = parse_time(data.get('appointmentTime'))
        contact_number = data.get('contactNumber')
        user_notes = data.get('additionalInfo')
        
        appointment = Appointment.objects.create(
            user=user,
            appointment_type=appointment_type,
            date=appointment_date,
            time=appointment_time,
            contact_number=contact_number,
            user_notes=user_notes
        )
        
        return JsonResponse({'status': 'success', 'appointment_id': appointment.id})
    else:
        return JsonResponse({'status': 'error'}, status=400)

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)  
    if request.method == "POST":
        appointment.delete()
        return redirect(VIEW_APPOINTMENTS)
    else:
        return redirect(VIEW_APPOINTMENTS)