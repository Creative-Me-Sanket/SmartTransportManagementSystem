# Generated by Django 3.2.7 on 2021-09-22 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_driverprofile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvehicle',
            name='time',
        ),
    ]
