# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
        ('venues', '0001_initial'),
        ('availability', '0003_auto_20160103_1927'),
        ('breakqual', '0003_auto_20160103_1927'),
        ('participants', '0002_auto_20160103_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='active_venues',
            field=models.ManyToManyField(through='availability.ActiveVenue', to='venues.Venue'),
        ),
        migrations.AddField(
            model_name='round',
            name='break_category',
            field=models.ForeignKey(blank=True, help_text='If elimination round, which break category', null=True, on_delete=django.db.models.deletion.CASCADE, to='breakqual.BreakCategory'),
        ),
        migrations.AddField(
            model_name='round',
            name='checkins',
            field=models.ManyToManyField(related_name='checkedin_rounds', through='availability.Checkin', to='participants.Person'),
        ),
        migrations.AddField(
            model_name='round',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='division',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
        migrations.AddField(
            model_name='division',
            name='venue_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='venues.VenueGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='round',
            unique_together=set([('tournament', 'seq')]),
        ),
        migrations.AlterIndexTogether(
            name='round',
            index_together=set([('tournament', 'seq')]),
        ),
        migrations.AlterUniqueTogether(
            name='division',
            unique_together=set([('tournament', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='division',
            index_together=set([('tournament', 'seq')]),
        ),
    ]
