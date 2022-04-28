from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.

# => in the if statement I am simply saying that if the request method is POST, it should do all the body of the if statement else it should remain on the user registration form.

def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.Post)
        # => the below line is to check if the form has passed all it's validations checked, then it can be saved
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'welcome {username}!')
            # => we redirect the user to home so that the user will know their form has been submitted
            return redirect('adoption-home')
    else:
        form = UserRegistrationForm

    data = {'form':form}
    return render(req,'registration.html', data)

# => now we have to go and create our template folder so that we can create  registration.html file
