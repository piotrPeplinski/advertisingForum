from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
# auth


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm()})
    else:  # POST
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST.get(
                    'username'), password=request.POST.get('password2'))
            except IntegrityError:
                error = 'This username is already taken. Try using different one.'
                return render(request, 'register.html', {'form': UserCreationForm(), 'error': error})
            else:  # wykonuje sie kiedy w try nie dojdzie do bledu
                user.save()
                # login user
                return redirect('home')
        else:
            error = 'Passwords did not match. Try again.'
            return render(request, 'register.html', {'form': UserCreationForm(), 'error': error})


def log(request):
    if request.method == 'GET':
        return render(request, 'log.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Username or password is wrong. Try again.'
            return render(request, 'log.html', {'form': AuthenticationForm(), 'error': error})

# ads


def home(request):
    return render(request, 'home.html')
