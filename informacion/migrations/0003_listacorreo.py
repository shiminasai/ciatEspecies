# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-17 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informacion', '0002_auto_20161202_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaCorreo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'Lista correo',
                'verbose_name_plural': 'Lista de correos',
            },
        ),
    ]