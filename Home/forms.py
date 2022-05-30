from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import  User, UserProfile

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
    
    
    
    
 
class editprofileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email',)
	password=None
	first_name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	last_name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	username = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.EmailInput(attrs={
			'class' :'form-control'
			}))
	
	
class changeDpForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'   