# Generated by Django 3.2.9 on 2021-11-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_homiy_tashkilot'),
    ]

    operations = [
        migrations.AddField(
            model_name='homiy',
            name='sarflangan_summa',
            field=models.IntegerField(default=0),
        ),
    ]
