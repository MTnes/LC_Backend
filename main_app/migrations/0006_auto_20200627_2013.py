# Generated by Django 2.2.13 on 2020-06-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200627_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media_content',
            name='media_content',
            field=models.ImageField(blank=True, default='settings.MEDIA_ROOT/logos/anonymous.jpg', null=True, upload_to='content'),
        ),
    ]
