# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-29 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bank_card',
            field=models.CharField(default='', max_length=35, verbose_name='银行卡'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bank_name',
            field=models.CharField(default='', max_length=10, verbose_name='银行名字'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bank_user_name',
            field=models.CharField(default='', max_length=10, verbose_name='银行卡用户名'),
        ),
    ]
