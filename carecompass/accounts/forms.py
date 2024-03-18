from django import forms
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.core.exceptions import ValidationError
from .models import User

class PatientSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gp_code', 'password']

    def __init__(self, *args, **kwargs):
        super(PatientSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'John'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Doe'})
        self.fields['email'].widget.attrs.update({'placeholder': 'john@mail.com'})
        self.fields['gp_code'].widget.attrs.update({'placeholder': '12345'})
        self.fields['password'].widget.attrs.update({'placeholder': '*********'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Please enter an email address.')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already in use.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise ValidationError('First name should only contain letters.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise ValidationError('Last name should only contain letters.')
        return last_name
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = False
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gp_code']

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name')

class UserChangeForm(DjangoUserChangeForm):
    class Meta(DjangoUserChangeForm.Meta):
        model = User
        fields = '__all__'