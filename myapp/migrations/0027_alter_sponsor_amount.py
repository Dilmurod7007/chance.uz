# Generated by Django 3.2.9 on 2021-11-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_remove_student_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='amount',
            field=models.IntegerField(default=1000000, max_length=100, null=True),
        ),
    ]
