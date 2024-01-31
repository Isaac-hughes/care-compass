from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def book_appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments:view_appointments')  # Redirect to view appointments
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('date_time')
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

def admin_view_appointments(request):
    if request.user.is_admin:
        appointments = Appointment.objects.all().order_by('date_time')
        return render(request, 'appointments/admin_view_appointments.html', {'appointments': appointments})
    else:
        return redirect('some_error_page')  # or handle permission denied
