# Generated by Django 3.1.2 on 2020-11-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0005_auto_20201116_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='appointments',
            field=models.PositiveIntegerField(blank=True, default=None),
        ),
    ]