# Generated by Django 3.2.9 on 2021-11-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20211112_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='my_type',
            field=models.CharField(choices=[('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd'), ('5', 'e')], default='a', max_length=1),
        ),
    ]
