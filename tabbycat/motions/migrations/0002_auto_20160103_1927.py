# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
        ('draw', '0003_auto_20160103_1927'),
        ('results', '0001_initial'),
        ('motions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motion',
            name='divisions',
            field=models.ManyToManyField(blank=True, to='tournaments.Division'),
        ),
        migrations.AddField(
            model_name='motion',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round'),
        ),
        migrations.AddField(
            model_name='debateteammotionpreference',
            name='ballot_submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.BallotSubmission'),
        ),
        migrations.AddField(
            model_name='debateteammotionpreference',
            name='debate_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draw.DebateTeam'),
        ),
        migrations.AddField(
            model_name='debateteammotionpreference',
            name='motion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.Motion'),
        ),
        migrations.AlterUniqueTogether(
            name='debateteammotionpreference',
            unique_together=set([('debate_team', 'preference', 'ballot_submission')]),
        ),
    ]
