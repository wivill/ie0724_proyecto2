from django.db import models
from django.contrib.auth.models import User
GENDERS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]


# Create your models here.
class usuario(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDERS)
    place = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=9)
    age = models.PositiveIntegerField(blank=True)
    allergies = models.CharField(max_length=60, blank=True)
