# Generated by Django 4.1.1 on 2022-10-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCreditos', '0005_delete_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='RES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=25)),
                ('comercio_res', models.CharField(max_length=25)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
    ]