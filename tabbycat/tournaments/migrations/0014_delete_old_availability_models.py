# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0013_remove_tournament_release_all'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='active_adjudicators',
        ),
        migrations.RemoveField(
            model_name='round',
            name='active_teams',
        ),
        migrations.RemoveField(
            model_name='round',
            name='active_venues',
        ),
        migrations.RemoveField(
            model_name='round',
            name='checkins',
        ),
    ]
