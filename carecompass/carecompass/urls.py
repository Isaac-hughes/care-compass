from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from accounts.views import custom_handler404, custom_handler500

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
]
