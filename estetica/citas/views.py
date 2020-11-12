from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import usuario, barber #, appointment
from .forms import userForm


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
