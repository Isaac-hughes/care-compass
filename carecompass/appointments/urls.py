from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.book_appointment_view, name='book_appointment'),
    path('view/', views.view_appointments, name='view_appointments'),
    path('admin_view/', views.admin_view_appointments, name='admin_view_appointments'),
]
