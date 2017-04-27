from django.shortcuts import render

# Create your views here.
def register(request):
    if request.user.is_authenticated():
        return redirect(home)
    registration_form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            datas={}
            datas['username']=form.cleaned_data['username']
            datas['email']=form.cleaned_data['email']
            datas['password1']=form.cleaned_data['password1']

            #We generate a random activation key
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            usernamesalt = datas['username']
            if isinstance(usernamesalt, unicode):
                usernamesalt = usernamesalt.encode('utf8')
            datas['activation_key']= hashlib.sha1(salt+usernamesalt).hexdigest()

            datas['email_path']="/ActivationEmail.txt"
            datas['email_subject']="Activation your account"

            form.sendEmail(datas)
            form.save(datas) #Save the user and his profile

            request.session['registered']=True #For display purposes
            return redirect(home)
        else:
            registration_form = form #Display form with error messages (incorrect fields, etc)
    return render(request, 'siteApp/register.html', locals())