# Generated by Django 3.2.9 on 2021-11-15 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_contracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
    ]
