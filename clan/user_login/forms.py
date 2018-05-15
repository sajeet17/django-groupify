from django.contrib.auth.models import User
from django import forms
from .models import UserInfo

class UserForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ["username","email","password"]


class UserInfoForm(forms.ModelForm):
	username = forms.CharField(widget=forms.HiddenInput)
	
	class Meta:
		model = UserInfo
		fields = ['first_name','last_name', 'age' ,'description', 'profile_picture','username']

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30)
	password = forms.CharField(label="Password", widget= forms.PasswordInput)