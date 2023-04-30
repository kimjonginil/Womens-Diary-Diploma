from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from account.models import User


def SignIn(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            return redirect('sign-in')
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=name,
                password=password
            )
            user.save()
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            return redirect('sign-in')

    return render(request, 'main/signin.html')


def SignOut(request):
    logout(request)
    return redirect('/')
