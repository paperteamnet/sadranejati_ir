# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.TextField(null=True),
        ),
    ]