# Generated by Django 2.2.4 on 2020-07-22 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_user_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
    ]
