# Generated by Django 3.2.3 on 2022-04-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0005_employee_hiredate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='hiredate',
            new_name='hire_date',
        ),
    ]
