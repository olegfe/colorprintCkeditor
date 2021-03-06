# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200413_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Полное содержание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 22, 19, 17, 44, 853370), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 22, 19, 17, 44, 854368), verbose_name='Дата'),
        ),
    ]
