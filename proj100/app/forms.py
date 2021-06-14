from django import forms

from django.contrib.auth.models import User

from .models import UserProfile

class SignupForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=['mobile','city','profpic']