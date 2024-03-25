from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import PatientSignUpForm, PatientUpdateForm
from appointments.models import Appointment

# route constants
LOGIN = 'accounts:login'
DASHBOARD = 'accounts:dashboard'

def signup_view(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD)
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            login(request, user)
            return redirect(DASHBOARD) 
    else:
        form = PatientSignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(DASHBOARD)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def landing_view(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD)
    return render(request, 'landing.html')

@login_required
def dashboard_view(request):
    next_appointment = Appointment.objects.order_by('date', 'time').first()
    
    return render(request, 'accounts/dashboard.html', {'next_appointment': next_appointment})

def logout_view(request):
    logout(request)
    return redirect(LOGIN) 


@login_required
def account_management_view(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:account_management')
    else:
        form = PatientUpdateForm(instance=request.user)

    return render(request, 'accounts/account_management.html', {'form': form})

def custom_handler404(request, exception):
    return render(request, '404.html', {}, status=404)


def custom_handler500(request):
    return render(request, '500.html', {}, status=500)
