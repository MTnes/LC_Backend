# Generated by Django 2.2.13 on 2020-06-20 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200619_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
    ]
