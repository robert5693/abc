# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=50, null=True, verbose_name='Titulo'),
        ),
    ]