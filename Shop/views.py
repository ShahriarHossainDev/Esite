from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User login success')
            return redirect('home')
        else:
            messages.error(request, '!Add new user!')
            return redirect('registration')

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, '!Add new user name!')
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
                messages.error(request, '!Add new email!')
                return redirect('registration')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                user.set_password(password)
                user.save()

                messages.success(request, 'User create success')
                return redirect('login')
        else:
            messages.error(request, '!Confirm password do not mach with Password!')
            return redirect('registration')

    return render(request, 'registration.html')


def logout(request):
    messages.error(request, '!Your user is logout!')
    auth.logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'profile.html')
