import uuid

from django.contrib import messages
from .models import *
from django.contrib.auth import login, logout
from .helpers import *
from .forms import *
from django.shortcuts import redirect, render


def home(request):
    return render(request, "authentication/index.html")


def signin(request):
    try:
        form = SignInForm(request, data=request.POST)
        context = {'form': form}
        if request.method == 'POST':
            if form.is_valid():
                user = form.cleaned_data.get('username')
                login(request, user)
                messages.success(request, 'You have successfully signed into your account')
                return redirect('/')
            else:
                print('Form is not valid')
                messages.error(request, 'Invalid login attempt, please check your credentials')
                return render(request, 'authentication/signin.html', context)
        else:
            return render(request, 'authentication/signin.html', context)
    except Exception as e:
        print(e)
    form = SignInForm(request, data=request.POST)
    context = {'form': form}
    return render(request, 'authentication/signin.html', context)


def signup(request):
    try:
        if request.method == 'GET':
            form = SignUpForm()
            context = {'form': form}
            return render(request, 'authentication/signup.html', context)
        if request.method == 'POST':
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + user)
                form.save()
                send_welcome_mail(email)
                return redirect('signin')
            else:
                print('Form is not valid')
                messages.error(request, 'Error Processing Your Request')
                context = {'form': form}
                return render(request, 'authentication/signup.html', context)
        return render(request, 'authentication/signup')
    except Exception as e:
        print(e)

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    return redirect('/')


# @login_required(login_url='signin')
# def Home(request):
#    return render(request , 'home.html')


def password_reset_request(request):
    try:
        if request.method == "POST":
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                if not User.objects.filter(email=email).first():
                    user_obj = User.objects.get(email=email)
                    token = str(uuid.uuid4())
                    profile_obj = Profile.objects.get(user=user_obj)
                    profile_obj.forget_password_token = token
                    profile_obj.save()
                    send_reset_password_mail(email, token, profile_obj)
            else:
                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="main/password/password_reset.html",
                              context={"password_reset_form": password_reset_form})
        else:
            print('Form not Valid')
            form = PasswordResetForm(request, data=request.POST)
            context = {'form': form}
            return render(request, 'authentication/password/password_reset_done.html', context)
    except Exception as e:
        print(e)

    form = PasswordResetForm(request, data=request.POST)
    context = {'form': form}
    return render(request, 'authentication/password/password_reset_done.html', context)
