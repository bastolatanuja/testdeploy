from django import forms
from django.contrib.auth import get_user_model
from .models import  User

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
    
    
