# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0011_auto_20180406_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irbSite.User'),
        ),
    ]
