# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-30 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='end',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evento',
            name='start',
            field=models.CharField(max_length=50),
        ),
    ]
