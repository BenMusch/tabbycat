# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0006_delete_old_availability_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roundavailability',
            options={'verbose_name': 'round availability', 'verbose_name_plural': 'round availabilities'},
        ),
        migrations.AlterField(
            model_name='roundavailability',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='roundavailability',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='object id'),
        ),
        migrations.AlterField(
            model_name='roundavailability',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round', verbose_name='round'),
        ),
    ]
