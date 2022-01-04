from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from .helpers import send_forget_password_mail, send_welcome_mail

def home(request):

    return render(request, "authentication/index.html")

def signin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.success(request, 'Both Username and Password are required.')
                return redirect('signin')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('signin')
        
        
            user = authenticate(username = username , password = password)
            
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('signin')
        
            login(request , user)
            return redirect('/')
        
    except Exception as e:
        print(e)
    
    return render(request, "authentication/signin.html")



def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_confirmation = request.POST.get('pasword_confirmation')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username Already Exists.')
                return redirect('signup')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email Already Exists.')
                return redirect('signup')

            if password != password_confirmation:
                messages.success(request, 'Password Mismatch')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
    
            profile_obj = Profile.objects.create(user = user_obj )
            profile_obj.save()
            
            send_welcome_mail(email)
            return redirect('signin')

        except Exception as e:
            print(e)

    except Exception as e:
            print(e)

    return render(request , 'authentication/signup.html')


def signout(request):
    logout(request)
    return redirect('/')


#@login_required(login_url='signin')
#def Home(request):
#    return render(request , 'home.html')



def change_password(request , token):
    context = {}
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            password = request.POST.get('password')
            password_confirmation = request.POST.get('password_confirmation')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}')
                
            
            if  password != password_confirmation:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change_password/{token}')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(password)
            user_obj.save()
            return redirect('signin')
               
    except Exception as e:
        print(e)
    return render(request , 'authentication/change_password.html' , context)


import uuid
def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('forgot_password')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email has been sent.')
            return redirect('forgot_password')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'authentication/forgot_password.html')