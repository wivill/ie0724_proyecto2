from django import forms
from .models import usuario


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
