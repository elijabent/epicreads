from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def register_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    elif request.method == 'GET':
        return render(request, 'users/register.html')

def login_request(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'users/login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
                print('error1')
        else:
            messages.error(request, "Invalid username or password")
            print('error2')
            print(form.error_messages)

def logout_request(request):
    logout(request)
    messages.info(request, "User logged out")
    return redirect("/")