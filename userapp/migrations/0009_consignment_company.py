# Generated by Django 3.2.7 on 2021-09-22 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_remove_tvehicle_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignment',
            name='company',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='userapp.packerprofile'),
            preserve_default=False,
        ),
    ]