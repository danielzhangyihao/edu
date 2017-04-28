from django import forms
from django.core.validators import validate_email
from user.models import MyUser

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

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")

		return self.cleaned_data

	def save(self, datas):
		u = settings.AUTH_USER_MODEL.objects.create_user(datas['email'],
                                     datas['password1'], datas['last_name'], datas['first_name'])
		u.is_active = False
		u.activation_key=datas['activation_key']
		u.key_expires=datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
		u.save()
		return u

	def sendEmail(self, datas):
		c = Context({'activation_code':datas['activation_key'],'username':datas['username']})
		f = open(MEDIA_ROOT+datas['email_path'], 'r')
		t = Template(f.read())
		f.close()
		message=t.render(c)
		#print unicode(message).encode('utf8')
		send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [datas['email']], fail_silently=False)