from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm  # You may need to create these forms

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_admin', 'is_staff']
    list_filter = ['is_admin', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'gp_code')}),
        ('Permissions', {'fields': ('is_staff', 'is_admin', 'is_superuser')}),
        # Add more fieldsets as needed
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
