from django import forms
from django.core.validators import validate_email
from user.models import MyUser
from django.core.mail import send_mail
import django.contrib.auth
import datetime

class RegistrationForm(forms.Form):
	last_name = forms.CharField(label='Last name', max_length=100)
	first_name = forms.CharField(label='First name', max_length=100)
	email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control input-perso'}),max_length=100,error_messages={'invalid': ("Email invalide.")},validators=[validate_email])
	password1 = forms.CharField(label='Password', max_length=50, min_length=6, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', max_length=50, min_length=6, widget=forms.PasswordInput)

	class Meta:
		model = MyUser

	def clean(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		email = self.cleaned_data.get('email')

		if django.contrib.auth.get_user_model().objects.filter(email=email).exists():
			raise forms.ValidationError({'email':["Email already exists"]})

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError({'password1':["Passwords don't match"]})

		return self.cleaned_data

	def save(self, datas):
		u = django.contrib.auth.get_user_model().objects.create_user(datas['email'],
                                     datas['password1'], datas['last_name'], datas['first_name'])

		u.activation_key=datas['activation_key']
		u.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
		u.save()
		return u

	def sendEmail(self, datas):
		send_mail(datas['email_subject'], "Please activate your account with this activation_code:" + datas['activation_key'], 'yourdomain <no-reply@yourdomain.com>', [datas['email']], fail_silently=False)

class SigninForm(forms.Form):
	email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control input-perso'}),max_length=100,error_messages={'invalid': ("Email invalide.")},validators=[validate_email])
	password=forms.CharField(label='Password', max_length=50, min_length=6, widget=forms.PasswordInput)

class ActivationForm(forms.Form):
	activation_code=forms.CharField(label='Activation code', min_length=5)