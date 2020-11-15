from django.shortcuts import render, redirect
# from django.http import HttpResponse, Http404
from django.http import Http404
from .models import usuario
from .forms import userForm
from .new_user_form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required


# Create your views here.
def new(request):
    new_form = userForm()
    if request.method == 'POST':
        filled_form = userForm(request.POST)
        if filled_form.is_valid():
            new_user = filled_form.save()
            note = (
                'Usuario con identificador \'{}\' fue creado exitosamente.\n'
                'Nombre: {}'.format(
                    new_user.pk, filled_form.cleaned_data['name']
                )
            )
        else:
            note = 'Formulario inválido'
        return render(
            request,
            'new.html',
            {
                'personform': new_form,
                'note': note,
            }
        )
    else:
        return render(
            request,
            'new.html',
            {
                'personform': new_form,
                'note': 'Hola!'
            }
        )


def show(request, pk=None):
    if pk is not None:
        try:
            user = usuario.objects.get(pk=pk)
        except usuario.DoesNotExist:
            raise Http404('Usuario con pk {} no existe'.format(pk))
        return render(
            request,
            'show.html',
            {
                'object_pk': user.pk,
                'object_name': user.name,
                'object_age': user.age,
            }
        )

    else:
        users_dict = {}
        for user in usuario.objects.all():
            users_dict[user.name] = {
                'pk': user.pk,
                'age': user.age
            }

        return render(
            request,
            'show.html',
            {
                'users_dict': users_dict
            }
        )


# def home(request):
#     return render(
#         request, 'home.html'
#     )


# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registro exitoso." )
# 			return redirect("home.html")
# 		messages.error(
#             request,
#             "Su registro ha fallado. Información inválida."
#         )
# 	form = NewUserForm
# 	return render (
#         request=request,
#         template_name="signup.html",
#         context={"register_form":form}
#     )
 
 
# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("home.html")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(
#         request=request,
#         template_name="login.html",
#         context={"login_form":form}
#      )


# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("home.html")
