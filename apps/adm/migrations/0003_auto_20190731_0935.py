# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-31 09:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('adm', '0002_auto_20190730_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='assettype',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assetType', to='users.Structure', verbose_name='资产到期提醒部门'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='dueDate',
            field=models.DateField(blank=True, default=datetime.date(2019, 7, 31), null=True, verbose_name='到期日期'),
        ),
    ]
