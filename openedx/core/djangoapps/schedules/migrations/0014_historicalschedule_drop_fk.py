# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-09 17:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0013_historicalschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='HistoricalSchedule',
            name='history_user',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
