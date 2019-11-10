from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signin/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signin/signup.html', {'error': 'Passwords do not match, please try again'})

    else:
        return render(request, 'signin/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin/login.html', {'error': 'incorrect username and password'})
    else:
        return render(request, 'signin/login.html')


def logout(request):
    #change this
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signin/logout.html')