# Generated by Django 3.1.2 on 2020-11-16 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0007_auto_20201116_0200'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NameBarber',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='scheduled_appointments',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='citas.nameuser'),
        ),
    ]
