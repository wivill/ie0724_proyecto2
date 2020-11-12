from django import forms
from .models import usuario #, appointment, barber

class userForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'name',
            'gender',
            'place',
            'phone_number',
            'age',
            'allergies',
        ]

        labels = {
            'name': 'Nombre',
            'gender': 'Género',
            'place': 'Lugar',
            'phone_number': 'Número de teléfono',
            'age': 'Edad',
            'allergies': 'Alergias',
        }
"""
class appointmentForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = [
            'hour',
            'date',
            'barber',
            'user',
        ]

        labels = {
            'hour': 'Hora',
            'date': 'Fecha',
            'barber': 'Estilista',
            'user': 'Usuario',

        }

class barberForm(forms.ModelForm):
    class Meta:
        model = barber
        fields = [
            'name',
            'gender',
            'phone_number',
            'age',
        ]

        labels = {
            'name': 'Nombre',
            'gender': 'Género',
            'phone_number': 'Número de teléfono',
            'age': 'Edad',
        }
"""