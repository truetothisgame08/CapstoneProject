# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irbSite', '0012_auto_20180406_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, default=52, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
