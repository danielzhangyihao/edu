from django.shortcuts import render
from .forms import RegistrationForm, SigninForm
import hashlib
import random
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.backends import AllowAllUsersModelBackend

# Create your views here.
def register(request):
    if request.user.is_authenticated():
        return redirect('/home/')
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
            datas['email_subject']="Activation your account"

            form.sendEmail(datas)
            form.save(datas) #Save the user and his profile

            request.session['registered']=True #For display purposes
            return redirect('/home/')
        else:
            registration_form = form #Display form with error messages (incorrect fields, etc)
    return render(request, 'signup.html', locals())

#def activate(request):

def signin(request):
    signin_form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else: 
                signin_form = form
                messages.warning(request, 'Please correct the error below.')
                return redirect('/home/')
        else:
            signin_form = form
    return render(request, 'login.html', locals())

def signout(request):
    logout(request)
    return redirect('/home/')

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()[:5]

def login(request):
    #@TODO: Fill in request handling logic
    return render(request, 'login.html', locals())
