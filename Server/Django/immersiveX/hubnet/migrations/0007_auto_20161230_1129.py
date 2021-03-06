# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubnet', '0006_auto_20161229_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='midpoint1',
        ),
        migrations.RemoveField(
            model_name='path',
            name='midpoint2',
        ),
        migrations.RemoveField(
            model_name='path',
            name='midpoint3',
        ),
        migrations.AddField(
            model_name='midpoint',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='path',
            name='midpoint',
            field=models.ManyToManyField(related_name='midpoint', to='hubnet.Midpoint'),
        ),
    ]
