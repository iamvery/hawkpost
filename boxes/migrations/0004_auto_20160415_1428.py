# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0003_box_closed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='closed',
        ),
        migrations.AddField(
            model_name='box',
            name='status',
            field=models.IntegerField(choices=[(10, 'Open'), (20, 'Expired'), (30, 'Sent'), (40, 'Closed')], default=10),
        ),
    ]