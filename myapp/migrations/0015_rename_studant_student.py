# Generated by Django 3.2.9 on 2021-11-13 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_sponsor_my_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Studant',
            new_name='Student',
        ),
    ]
