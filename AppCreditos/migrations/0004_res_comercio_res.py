# Generated by Django 4.1.1 on 2022-10-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCreditos', '0003_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='res',
            name='comercio_res',
            field=models.CharField(default='', max_length=25),
        ),
    ]
