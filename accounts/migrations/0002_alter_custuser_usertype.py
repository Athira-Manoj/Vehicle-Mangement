# Generated by Django 4.1.5 on 2023-08-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='usertype',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], max_length=100),
        ),
    ]
