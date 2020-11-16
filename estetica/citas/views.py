from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import usuario, barber, appointment
from .forms import userForm, barberForm, appointmentForm


# Create your views here.
# ////////////////////////////////////
# Usuarios
# ////////////////////////////////////
def new_user(request):
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
            'new_user.html',
            {
                'personform': new_form,
                'note': note,
            }
        )
    else:
        return render(
            request,
            'new_user.html',
            {
                'personform': new_form,
                'note': 'Creación de nuevo usuario'
            }
        )


def show_user(request, pk=None):
    if pk is not None:
        try:
            user = usuario.objects.get(pk=pk)
        except usuario.DoesNotExist:
            raise Http404('Usuario con pk {} no existe'.format(pk))
        return render(
            request,
            'show_user.html',
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
            'show_user.html',
            {
                'users_dict': users_dict
            }
        )

# ////////////////////////////////////
# Estilistas
# ////////////////////////////////////


def new_stylist(request):
    new_form = barberForm()
    if request.method == 'POST':
        filled_form = barberForm(request.POST)
        if filled_form.is_valid():
            new_user = filled_form.save()
            note = (
                'Barbero con identificador \'{}\' fue creado exitosamente.\n'
                'Nombre: {}'.format(
                    new_user.pk, filled_form.cleaned_data['name']
                )
            )
        else:
            note = 'Formulario inválido'
        return render(
            request,
            'new_barber.html',
            {
                'personform': new_form,
                'note': note,
            }
        )
    else:
        return render(
            request,
            'new_barber.html',
            {
                'personform': new_form,
                'note': 'Creación de nuevo barbero'
            }
        )


def show_stylist(request, name=None):
    if name is not None:
        try:
            user = barber.objects.get(name=name)
        except barber.DoesNotExist:
            raise Http404('Usuario con nombre {} no existe'.format(name))
        return render(
            request,
            'show_barber.html',
            {
                'object_pk': barber.pk,
                'object_name': barber.name,
                'object_age': barber.age,
                'phone_number': barber.phone_number,
                'gender': barber.gender,
            }
        )

    else:
        users_dict = {}
        for user in barber.objects.all():
            users_dict[user.name] = {
                'object_pk': barber.pk,
                'object_name': barber.name,
                'object_age': barber.age,
                'phone_number': barber.phone_number,
                'gender': barber.gender,
            }

        return render(
            request,
            'show_barber.html',
            {
                'users_dict': users_dict
            }
        )

# ////////////////////////////////////
# Citas
# ////////////////////////////////////

def show_appointments(request, name=None):
    if name is not None:
        try:
            user = appointment.objects.get(name=name)
        except appointment.DoesNotExist:
            raise Http404('No existen citas para el usuario {} no existe'.format(name))
        return render(
            request,
            'show_appointments.html',
            {
                'object_pk': appointment.pk,
                'object_name': appointment.name,
                'object_age': appointment.age,
                'phone_number': appointment.phone_number,
                'gender': appointment.gender,
            }
        )

    else:
        users_dict = {}
        for user in appointment.objects.all():
            users_dict[user.name] = {
                'object_pk': appointment.pk,
                'object_name': appointment.name,
                'object_age': appointment.age,
                'phone_number': appointment.phone_number,
                'gender': appointment.gender,
            }

        return render(
            request,
            'show_appointments.html',
            {
                'users_dict': users_dict
            }
        )

def new_appointment(request):
    new_form = appointmentForm()
    if request.method == 'POST':
        filled_form = appointmentForm(request.POST)
        if filled_form.is_valid():
            new_user = filled_form.save()
            note = (
                'Cita con identificador \'{}\' fue creada exitosamente.\n'
                'Fecha: {}\n'
                'Hora: {}\n'
                'Barbero: {}'.format(
                    new_user.pk, filled_form.cleaned_data['date'], filled_form.cleaned_data['hour'], filled_form.cleaned_data['barber'],
                )
            )
        else:
            note = 'Formulario inválido'
        return render(
            request,
            'new_appointment.html',
            {
                'personform': new_form,
                'note': note,
            }
        )
    else:
        return render(
            request,
            'new_appointment.html',
            {
                'personform': new_form,
                'note': 'Creación de nueva cita'
            }
        )





    """
    path('show_stylist/', views.show_stylist, name="show_stylist"),
    path('new_appointment/', views.new_appointment, name="new_appointment"),
    path('show_appointments/', views.show_appointments, name="show_appointments"),
    path('new_stylist/', views.new_stylist, name="new_stylist"),
    """

