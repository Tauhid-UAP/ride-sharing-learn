# Generated by Django 3.2 on 2021-09-06 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_generaluser_activated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaluser',
            old_name='activated',
            new_name='is_activated',
        ),
    ]