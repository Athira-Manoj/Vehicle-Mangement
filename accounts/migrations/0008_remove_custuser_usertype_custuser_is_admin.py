# Generated by Django 4.1.5 on 2023-08-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_custuser_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custuser',
            name='usertype',
        ),
        migrations.AddField(
            model_name='custuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='admin status'),
        ),
    ]
