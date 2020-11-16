from django.contrib import admin
from .models import usuario, barber, appointment
# Register your models here.
admin.site.register(usuario)
admin.site.register(barber)
admin.site.register(appointment)
