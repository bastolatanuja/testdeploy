from dataclasses import fields
from django import forms
from django.contrib.auth import get_user_model
from .models import  User, prescription

User = get_user_model()

class UserResgistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def get_id(self):
        return self.user.id
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]

    def get_id(self):
        return self.user.id
    
class UserResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def get_id(self):
        return self.user.id

class Prescription(forms.ModelForm):
    class Meta:
        model = prescription
        fields = ("__all__")
