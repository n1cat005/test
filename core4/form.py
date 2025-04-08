from django import forms
from .models import Contact, Register
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı daxil edin'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailinizi daxil edin'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınızı yazın', 'rows': 4}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['full_name','email', 'password', 'confirm_password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı daxil edin'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailinizi daxil edin'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            'confirm_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

