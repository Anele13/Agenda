# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-01 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0003_auto_20180930_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='aula',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='materia',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='persona',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
