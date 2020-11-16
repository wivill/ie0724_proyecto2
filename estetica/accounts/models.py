from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.db import models
from citas.models import usuario


class UserCreateForm(UserCreationForm):
    name = forms.CharField(max_length=60)
    gender = forms.CharField(max_length=1)
    place = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=9)
    age = forms.IntegerField()
    allergies = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'name',
            'gender',
            'place',
            'phone_number',
            'age',
            'allergies'
        )

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = usuario(
                                   user=user,
                                   name=self.cleaned_data['name'],
                                   gender=self.cleaned_data['gender'],
                                   age=self.cleaned_data['age'],
                                   place=self.cleaned_data['place'],
                                   phone_number=self.cleaned_data['phone_number'],
                                   allergies=self.cleaned_data['allergies']
                                   )
        user_profile.save()
        return user, user_profile
