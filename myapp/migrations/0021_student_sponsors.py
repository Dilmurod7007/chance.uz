# Generated by Django 3.2.9 on 2021-11-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_student_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sponsors',
            field=models.ManyToManyField(to='myapp.Sponsor'),
        ),
    ]