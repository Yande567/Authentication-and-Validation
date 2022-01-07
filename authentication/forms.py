from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg ', 'placeholder': 'Email'}), )
    first_name = forms.CharField(label='', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg', 'placeholder': 'First Name'}), )
    last_name = forms.CharField(label='', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg', 'placeholder': 'Last Name'}), )
    username = forms.CharField(label='', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg', 'placeholder': 'Username'}), )
    password1 = forms.CharField(label='', min_length=8, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control  input-lg col-md-6',
               'placeholder': 'Password'}), )
    password2 = forms.CharField(label='', min_length=8, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control  input-lg col-md-6',
               'placeholder': 'Confirm Password'}), )

    check = forms.BooleanField(label='', required=True, widget=forms.CheckboxInput(
         attrs={'class': 'row col-xs-4 col-sm-3 col-md-3 button-checkbox', 'placeholder': 'I Agree'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', ]


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg', 'placeholder': 'Username'}), )
    password = forms.CharField(label='', min_length=8, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-group form-control input-lg', 'placeholder': 'Password'}), )

    class Meta:
        model = User
        fields = ['username', 'password']


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-group form-control input-lg ', 'placeholder': 'Email'}), )

    class Meta:
        model = User
        fields = ['email']
