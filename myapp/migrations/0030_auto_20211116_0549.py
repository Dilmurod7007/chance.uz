# Generated by Django 3.2.9 on 2021-11-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20211116_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(choices=[('TTPU', 'Toshkent Turin Politxnika Universiteti'), ('TDSHI', 'Toshkent Davlat Sharqshunoslik Universiteti')], max_length=6000),
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
