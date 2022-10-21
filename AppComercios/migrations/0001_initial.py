# Generated by Django 4.1 on 2022-10-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('cuit', models.IntegerField()),
                ('rubro', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('ciudad', models.CharField(max_length=25)),
                ('provincia', models.CharField(max_length=25)),
                ('fecha_adhesion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
