from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .models import UserCreateForm


def welcome(request):
    # Si estamos identificados devolvemos el home
    if request.user.is_authenticated:
        return render(request, "home.html")

    return redirect('/login')


def signup(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(data=request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                do_login(request, user)
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/signup.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "registration/login.html", {'form': form})


def logout(request):
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
