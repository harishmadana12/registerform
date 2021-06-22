from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        user_name = request.POST['username']
        email_id = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'User name already taken')
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, 'Email id already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email_id,
                                                first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
