# Generated by Django 2.2.13 on 2020-06-24 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_testclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testclass',
            name='doc',
        ),
    ]