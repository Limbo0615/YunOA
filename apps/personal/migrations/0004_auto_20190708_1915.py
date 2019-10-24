# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20190705_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderlog',
            name='type',
            field=models.CharField(choices=[('0', '审批'), ('1', '报销')], default='0', max_length=10, verbose_name='日志类型'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='transport',
            field=models.CharField(blank=True, choices=[('0', '自己开车'), ('1', '大巴'), ('2', '火车'), ('3', '动车'), ('4', '飞机'), ('5', '轮船')], max_length=300, null=True, verbose_name='交通工具'),
        ),
    ]
