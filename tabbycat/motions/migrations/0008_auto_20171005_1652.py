# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0007_auto_20160723_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debateteammotionpreference',
            options={'verbose_name': 'debate team motion preference', 'verbose_name_plural': 'debate team motion preferences'},
        ),
        migrations.AlterModelOptions(
            name='motion',
            options={'ordering': ('seq',), 'verbose_name': 'motion', 'verbose_name_plural': 'motions'},
        ),
        migrations.AlterField(
            model_name='debateteammotionpreference',
            name='ballot_submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.BallotSubmission', verbose_name='ballot submission'),
        ),
        migrations.AlterField(
            model_name='debateteammotionpreference',
            name='debate_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.DebateTeam', verbose_name='debate team'),
        ),
        migrations.AlterField(
            model_name='debateteammotionpreference',
            name='motion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.Motion', verbose_name='motion'),
        ),
        migrations.AlterField(
            model_name='debateteammotionpreference',
            name='preference',
            field=models.IntegerField(db_index=True, verbose_name='preferences'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='divisions',
            field=models.ManyToManyField(blank=True, to='divisions.Division', verbose_name='divisions'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='flagged',
            field=models.BooleanField(default=False, help_text='For WADL: Allows for particular motions to be flagged as contentious', verbose_name='flagged'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='reference',
            field=models.CharField(help_text='Shortcode for the motion, e.g., "Bananas"', max_length=100, verbose_name='reference'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round', verbose_name='round'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='seq',
            field=models.IntegerField(help_text='The order in which motions are displayed', verbose_name='sequence number'),
        ),
        migrations.AlterField(
            model_name='motion',
            name='text',
            field=models.TextField(help_text='The full motion e.g., "This House would straighten all bananas"', max_length=500, verbose_name='text'),
        ),
    ]
