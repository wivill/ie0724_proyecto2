from django.shortcuts import render, redirect
# from django.http import HttpResponse, Http404
from django.http import Http404
from .models import usuario
from .forms import userForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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


def home(request):
    return render(
        request, 'home.html'
    )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(
        request,
        'signup.html',
        {'form': form}
    )
