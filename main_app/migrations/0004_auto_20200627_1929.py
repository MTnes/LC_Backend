# Generated by Django 2.2.13 on 2020-06-27 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_session_date_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_uploaded',
            field=models.DateField(default=datetime.date(2020, 6, 27)),
        ),
    ]