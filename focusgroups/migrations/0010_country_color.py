# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-02 21:54
from __future__ import unicode_literals

from django.db import migrations
import paintstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('focusgroups', '0009_auto_20170202_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='color',
            field=paintstore.fields.ColorPickerField(default=1, max_length=7),
            preserve_default=False,
        ),
    ]