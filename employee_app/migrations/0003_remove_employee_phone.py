# Generated by Django 3.2.3 on 2022-04-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
    ]
