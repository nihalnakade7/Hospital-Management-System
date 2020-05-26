from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views import generic
from .models import MyUsers

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            myuser = MyUsers.objects.get(user_id = user.id,)
            print(myuser.role)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            request.session['role'] = myuser.role
            return redirect('/')
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect('login')
        
    else:
        return render(request,'accounts/login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        user_type =int(request.POST['usertype'])
        role = ""
        print(user_type)

        if(user_type == 1):
            role = "Doctor"
        if(user_type == 2):
            role = "Patient"      
        messages.info(request,'')
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken') 
                return render(request,'accounts/register.html')      
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken') 
                return render(request,'accounts/register.html')    
            else:
                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save();
                myuser = MyUsers()
                myuser.role = role
                myuser.user = user
                myuser.save()
                print('user Created')
                return redirect("login")
                
        else:
            messages.info(request,'Password nad Confirm Password not matching') 
            return render(request,'accounts/register.html')    
    else:
        return render(request,'accounts/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



