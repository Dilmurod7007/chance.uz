# Generated by Django 3.2.9 on 2021-11-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20211113_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]