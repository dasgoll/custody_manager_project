from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('employees')
        else:
            return render(request, 'accounts/home.html')
    else:
        if request.user.is_authenticated:
            return redirect('employees')
        else:
            return render(request, 'accounts/home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
