from django import forms
from django.contrib import admin
from django.contrib.auth import(authenticate,get_user_model,login,logout,)
from User.models import User
CHOICES=[('Male','Male'),
         ('Female','Female')]
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user=authenticate(username=username, password=password)
		user_qs= User.objects.filter(username=username)
		if user_qs.count() == 1:
			user = user_qs.first()
		if not user:
			raise forms.ValidationError("This user doesn't exist.")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password.")
		if not user.is_active:
			raise forms.ValidationError("The user is no longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)
	

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email = forms.EmailField(required=True)
	Gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'placeholder': 'Choose your gender'}),choices=CHOICES)
	birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
	class Meta:
		model = User
		fields=['first_name','last_name','username','email','password','location','Gender','birth_date','bio','Image']


class UserImageform(forms.ModelForm):
	class Meta:
		model=User
		fields=['Image']