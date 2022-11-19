# Generated by Django 3.2.3 on 2022-04-14 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0004_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
