from django.db import models
GENDERS = [
    ('M', 'Hombre'),
    ('F', 'Mujer'),
    ('O', 'Otro')
]

schedules = [
    ('7:15-8:00'),
    ('8:15-9:00'),
    ('10:15-11:00'),
    ('11:15-12:00'),
    ('13:15-14:00'),
    ('14:15-15:00'),
    ('15:15-16:00'),
]

barbers = [
    ('Tony'),
    ('Willy'),
    ('Bernardo'),
]

program_appointments = {
    
}

# Create your models here.
class usuario(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDERS)
    place = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=9)
    age = models.PositiveIntegerField(blank=True)
    allergies = models.CharField(max_length=60, blank=True)

# Create your models here.
class barber(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=GENDERS)
    phone_number = models.CharField(max_length=9)
    age = models.PositiveIntegerField(blank=True)

class NameUser(usuario):
   class Meta:
      proxy = True

   def __str__(self):
        return str(self.name)

   def __unicode__(self):
        return str(self.name)

class appointment(models.Model):
    hour = models.TimeField()
    date = models.DateField()
    barber = models.ForeignKey(barber, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(NameUser, blank=True, on_delete=models.DO_NOTHING)

