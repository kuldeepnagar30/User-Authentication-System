from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Profile


# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        unm = request.POST.get('username')
        eml = request.POST.get('email')
        pwd = request.POST.get('password')
        contact = request.POST.get('contact')

        try:
            User.objects.get(username=unm)
        
            return render(request,'signup.html',{'error':'Username already exists.'})
        
        except:
            user = User.objects.create_user (username=unm,first_name=name,email=eml,password=pwd)
            Profile.objects.create(
            user=user,
            contact=contact
            )
            user.save()
            
            return render(request, 'signin.html',{'success':'Account created successfully.'})
    else:
        return render (request,'signup.html')

def signin(request):
    if request.method == 'POST':
        
        unm = request.POST.get('username')
        pwd = request.POST.get('password') 

        user = auth.authenticate(request,username=unm,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('userhome')
        else:
            
            return render(request, 'signin.html', {'invalid': 'Invalid Username or Password.'})

    return render(request, 'signin.html')

def userhome(request):
     return render(request,'userhome.html')


def logout(request):
    auth.logout(request)
    return render(request,'index.html', {'log':'Logout successfully. '})