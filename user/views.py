from django.shortcuts import render
from .forms import RegistrationForm, SigninForm, ActivationForm
import hashlib
import random
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.user.is_authenticated():
        if request.user.is_active == False:
            return redirect('/activate')
        else:
            return redirect('/')
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
            user = authenticate(username=datas['email'], password=datas['password1'])
            login(request, user)

            request.session['registered']=True #For display purposes
            return redirect('/activate')
        else:
            registration_form = form #Display form with error messages (incorrect fields, etc)
    return render(request, 'signup.html', locals())

@login_required(login_url='/login/')
def activate(request):
    if request.user.is_active == True:
        messages.info(request, 'already activated')
        return redirect('/')
    activation_form = ActivationForm()
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            activation_code = form.cleaned_data['activation_code']
            if timezone.now() > request.user.key_expires:
                messages.warning(request, 'activation code expired')
            elif request.user.activation_key == activation_code: 
                request.user.is_active = true
                request.user.save()
                messages.success(request, 'activated successfully')
                return redirect('/')
            else:
                messages.warning(request, 'wrong code')
        else:
            activation_form = form
    return render(request, 'activation.html', locals())


def signin(request):
    if request.user.is_authenticated():
        if request.user.is_active == False:
            return redirect('/activate')
        else:
            return redirect('/')
    signin_form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_active == False:
                    return redirect('/activate')
                else:
                    return redirect('/')
            else: 
                signin_form = form
                messages.warning(request, 'incorrect credentials')
        else:
            signin_form = form
    return render(request, 'login.html', locals())

def signout(request):
    logout(request)
    return redirect('/')

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()[:5]
