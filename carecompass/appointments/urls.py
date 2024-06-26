from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.book_appointment_view, name='book_appointment'),
    path('view/', views.view_appointments, name='view_appointments'),
    path('admin_view/', views.admin_view_appointments, name='admin_view_appointments'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
]
