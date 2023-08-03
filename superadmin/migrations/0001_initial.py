# Generated by Django 4.1.5 on 2023-08-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Two Wheelers', 'Two'), ('Three Wheelers', 'Three'), ('Four Wheelers', 'Four')], max_length=100)),
                ('model', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
