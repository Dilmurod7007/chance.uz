# Generated by Django 3.2.9 on 2021-11-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_homiy_holati'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homiy',
            name='summa',
            field=models.CharField(choices=[('1 000 000', '1 000 000'), ('5 000 000', '5 000 000'), ('7 000 000', '7 000 000'), ('30 000 000', '30 000 000')], default='1 000 000', max_length=100),
        ),
    ]
