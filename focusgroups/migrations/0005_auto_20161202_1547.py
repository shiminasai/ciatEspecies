# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-02 15:47
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('focusgroups', '0004_focusgroup_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scientists',
            options={'verbose_name': 'Scientific', 'verbose_name_plural': 'Scientists'},
        ),
        migrations.AddField(
            model_name='organizations',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='direccion',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='organizaciones/'),
        ),
        migrations.AddField(
            model_name='organizations',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='focusgroups.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizations',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=450),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizations',
            name='telefono',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scientists',
            name='cargo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='cientificos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='focusgroups.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='perfil',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=450),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scientists',
            name='telefono',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]