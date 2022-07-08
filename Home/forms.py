from dataclasses import field, fields
from django import forms
from django.contrib.auth import get_user_model
<<<<<<< HEAD
from .models import  User, UserProfile, checkoutItems, prescription,CartItem,cashdevlivery
=======
from .models import  User, prescription, cashdevlivery
>>>>>>> e7bf551d183c050600ec9dcc8286f09bda897751

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

class Cashdelivery(forms.ModelForm):
    class Meta:
        model = cashdevlivery
        fields = ("__all__")

<<<<<<< HEAD
class changeDpForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ("__all__")

class cartEditform(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('number_of_products',)

class CheckoutItems(forms.ModelForm):
    class Meta:
        model = checkoutItems
        fields = ("__all__")
=======
>>>>>>> e7bf551d183c050600ec9dcc8286f09bda897751
