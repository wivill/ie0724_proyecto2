# Generated by Django 3.1.2 on 2020-11-16 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0011_appointmentsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='appointments',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='citas.appointmentsdata'
                                    ),
        ),
    ]
