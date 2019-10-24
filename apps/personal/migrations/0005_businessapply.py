# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-07-15 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('personal', '0004_auto_20190708_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('-1', '可以申请'), ('0', '等待审批'), ('1', '审批中'), ('2', '审批完成'), ('3', '审批被退回')], default='-1', max_length=10, verbose_name='审批状态')),
                ('transport', models.CharField(blank=True, choices=[('0', '自己开车'), ('1', '大巴'), ('2', '火车'), ('3', '动车'), ('4', '飞机'), ('5', '轮船')], max_length=300, null=True, verbose_name='交通工具')),
                ('becity', models.CharField(blank=True, max_length=300, null=True, verbose_name='出发地点')),
                ('destination', models.CharField(blank=True, max_length=300, null=True, verbose_name='目标地点')),
                ('people', models.CharField(blank=True, max_length=300, null=True, verbose_name='随行人员')),
                ('tran_fee', models.CharField(blank=True, max_length=12, verbose_name='交通费用')),
                ('acco_fee', models.CharField(blank=True, max_length=12, verbose_name='住宿费用')),
                ('food_fee', models.CharField(blank=True, max_length=12, verbose_name='餐饮费用')),
                ('rece_fee', models.CharField(blank=True, max_length=12, verbose_name='招待费用')),
                ('payee', models.CharField(blank=True, max_length=300, null=True, verbose_name='收款方')),
                ('bank_account', models.CharField(blank=True, max_length=30, null=True, verbose_name='银行账户')),
                ('bank_info', models.CharField(blank=True, max_length=300, null=True, verbose_name='开户行')),
                ('completion_info', models.TextField(null=True, verbose_name='完成情况')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='报销明细')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('cretor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business', to=settings.AUTH_USER_MODEL, verbose_name='申请人')),
                ('next_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_next_order', to=settings.AUTH_USER_MODEL, verbose_name='当前审批人')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business', to='users.Structure', verbose_name='申请时所在部门')),
                ('workorder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business', to='personal.WorkOrder', verbose_name='审批单')),
            ],
        ),
    ]
