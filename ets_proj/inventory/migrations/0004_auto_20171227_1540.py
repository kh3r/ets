# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20171227_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='category',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='manual',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='warranty',
            name='warranty_end_date',
            field=models.DateField(max_length=256),
        ),
        migrations.AlterField(
            model_name='warranty',
            name='warranty_start_date',
            field=models.DateField(max_length=256),
        ),
    ]
