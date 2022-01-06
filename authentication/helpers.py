from urllib import request

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import redirect, render


from django.conf import settings 


def send_forget_password_mail(email, token):
    subject = 'Your forgot password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change_password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def send_welcome_mail(email):
    subject = 'Welcome'
    message = f'Hi , welcome to our authentication website'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def send_reset_password_mail(user_email, token, user):
    subject = "Password Reset Requested"
    email_from = settings.EMAIL_HOST_USER
    email_template_name = "template/authentication/passwords/password_reset_email.txt"
    recipient_list = [user_email]
    c = {
        "email": user_email,
        'domain': '127.0.0.1:8000',
        'site_name': 'Website',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': token,
        'protocol': 'http',
    }

    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, email_from, recipient_list, fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

    return True
