# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-20 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='desc',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]
