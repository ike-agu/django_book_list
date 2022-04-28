from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# => this form we are creating will be imported to views
# =>  this are te requirements for django base form or foundation form
# => now we have to go create a registration View bc django does not give it to us by default
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']
