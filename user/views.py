from django.shortcuts import render
from .forms import RegistrationForm
import hashlib
import random
from django.utils.crypto import get_random_string

# Create your views here.
def register(request):
    if request.user.is_authenticated():
        return redirect(home)
    registration_form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            datas={}
            datas['last_name']=form.cleaned_data['last_name']
            datas['first_name']=form.cleaned_data['first_name']
            datas['email']=form.cleaned_data['email']
            datas['password1']=form.cleaned_data['password1']
            datas['activation_key']= generate_activation_key(datas['email'])
            datas['email_path']="/ActivationEmail.txt"
            datas['email_subject']="Activation your account"

            form.sendEmail(datas)
            form.save(datas) #Save the user and his profile

            request.session['registered']=True #For display purposes
            return redirect(home)
        else:
            registration_form = form #Display form with error messages (incorrect fields, etc)
    return render(request, 'signup.html', locals())

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()[:5]

def login(request):
    #@TODO: Fill in request handling logic
    return render(request, 'login.html', locals())
