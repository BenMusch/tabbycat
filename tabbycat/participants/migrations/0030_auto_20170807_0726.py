# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0020_auto_20170422_1511'),
        ('participants', '0030_auto_20170722_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name to be displayed, e.g., "ESL"', max_length=50, verbose_name='name')),
                ('slug', models.SlugField(help_text='Slug for URLs, e.g., "esl"', verbose_name='slug')),
                ('seq', models.IntegerField(help_text='The order in which the categories are displayed', verbose_name='sequence number')),
                ('limit', models.IntegerField(default=0, help_text='At most this many speakers will be shown on the public tab for this category, or use 0 for no limit', verbose_name='limit')),
                ('public', models.BooleanField(default=True, help_text='If checked, this category will be included in the speaker category tabs shown to the public', verbose_name='public')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament')),
            ],
            options={
                'verbose_name_plural': 'speaker categories',
                'verbose_name': 'speaker category',
                'ordering': ['tournament', 'seq'],
            },
        ),
        migrations.AlterModelOptions(
            name='adjudicator',
            options={'ordering': ['tournament', 'institution', 'name'], 'verbose_name': 'adjudicator', 'verbose_name_plural': 'adjudicators'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name'], 'verbose_name': 'institution', 'verbose_name_plural': 'institutions'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'region', 'verbose_name_plural': 'regions'},
        ),
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'speaker', 'verbose_name_plural': 'speakers'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['tournament', 'institution', 'short_reference'], 'verbose_name': 'team', 'verbose_name_plural': 'teams'},
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='adj_core',
            field=models.BooleanField(default=False, verbose_name='adjudication core'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='breaking',
            field=models.BooleanField(default=False, verbose_name='breaking'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='conflicts',
            field=models.ManyToManyField(related_name='adj_adj_conflicts', through='adjallocation.AdjudicatorConflict', to='participants.Team', verbose_name='team conflicts'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='independent',
            field=models.BooleanField(default=False, verbose_name='independent'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='institution_conflicts',
            field=models.ManyToManyField(related_name='adj_inst_conflicts', through='adjallocation.AdjudicatorInstitutionConflict', to='participants.Institution', verbose_name='institution conflicts'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='test_score',
            field=models.FloatField(default=0, verbose_name='test score'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='tournament',
            field=models.ForeignKey(blank=True, help_text='Adjudicators not assigned to any tournament can be shared between tournaments', null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='url_key',
            field=models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='abbreviation',
            field=models.CharField(default='', help_text='For extremely confined spaces, e.g., "Camb", "VicWgtn"', max_length=8, verbose_name='abbreviation'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='code',
            field=models.CharField(help_text='What the institution is typically called for short, e.g., "Cambridge", "Vic Wellington"', max_length=20, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(help_text='The institution\'s full name, e.g., "University of Cambridge", "Victoria University of Wellington"', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Region', verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='person',
            name='anonymous',
            field=models.BooleanField(default=False, help_text='Anonymous persons will have their name and team redacted on public tab releases', verbose_name='anonymous'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Gender is displayed in the adjudicator allocation interface, and nowhere else', max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=40, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pronoun',
            field=models.CharField(blank=True, help_text='If printing ballots using Tabbycat, there is the option to pre-print pronouns', max_length=10, verbose_name='pronoun'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='break_categories',
            field=models.ManyToManyField(blank=True, to='breakqual.BreakCategory', verbose_name='break categories'),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='divisions.Division', verbose_name='division'),
        ),
        migrations.AlterField(
            model_name='team',
            name='emoji',
            field=models.CharField(blank=True, choices=[('☕', '☕'), ('⛑', '⛑'), ('⛰', '⛰'), ('⛪', '⛪'), ('⛵', '⛵'), ('⛔', '⛔'), ('⛅', '⛅'), ('⛈', '⛈'), ('⛱', '⛱'), ('⛄', '⛄'), ('⚽', '⚽'), ('⛸', ''), ('⛏', '⛏'), ('😁', '😁'), ('😂', '😂'), ('😄', '😄'), ('😅', ''), ('😆', '😆'), ('😉', '😉'), ('😊', '😊'), ('😎', '😎'), ('😍', '😍'), ('😘', '😘'), ('😇', '😇'), ('😐', '😐'), ('😏', '😏'), ('😣', ''), ('😥', '😥'), ('😫', ''), ('😜', '😜'), ('😓', ''), ('😔', ''), ('😖', '😖'), ('😷', '😷'), ('😲', '😲'), ('😞', '😞'), ('😭', '😭'), ('😰', '😰'), ('😱', '😱'), ('😳', '😳'), ('😵', '😵'), ('😡', '😡'), ('👿', '👿'), ('👩', '👩'), ('👴', '👴'), ('👵', '👵'), ('👶', '👶'), ('👮', '👮'), ('👷', '👷'), ('👸', '👸'), ('💂', '💂'), ('🎅', '🎅'), ('👼', '👼'), ('👰', '👰'), ('🙅', '🙅'), ('🙆', '🙆'), ('🙋', '🙋'), ('🙇', '🙇'), ('🙌', '🙌'), ('🙏', '🙏'), ('💃', '💃'), ('💑', '💑'), ('👪', '👪'), ('👫', '👫'), ('👬', '👬'), ('👭', '👭'), ('💪', '💪'), ('👆', '👆'), ('✊', '✊'), ('✋', '✋'), ('👊', '👊'), ('👌', '👌'), ('👍', '👍'), ('👎', '👎'), ('👐', '👐'), ('💅', '💅'), ('👂', '👂'), ('👃', '👃'), ('👅', '👅'), ('👄', '👄'), ('💘', '💘'), ('💔', '💔'), ('💖', '💖'), ('💌', '💌'), ('💧', '💧'), ('💤', ''), ('💣', '💣'), ('💥', '💥'), ('💦', '💦'), ('💨', '💨'), ('💫', ''), ('👓', '👓'), ('👔', '👔'), ('👙', '👙'), ('👜', '👜'), ('👟', '👟'), ('👠', '👠'), ('👒', '👒'), ('🎩', '🎩'), ('💄', '💄'), ('💍', '💍'), ('💎', '💎'), ('👻', '👻'), ('💀', '💀'), ('👽', '👽'), ('👾', '👾'), ('💩', '💩'), ('🐵', ''), ('🙈', ''), ('🙉', ''), ('🙊', ''), ('🐶', '🐶'), ('🐩', ''), ('🐯', '🐯'), ('🐴', '🐴'), ('🐮', '🐮'), ('🐷', '🐷'), ('🐑', '🐑'), ('🐭', '🐭'), ('🐹', '🐹'), ('🐰', '🐰'), ('🐻', '🐻'), ('🐨', '🐨'), ('🐼', '🐼'), ('🐔', '🐔'), ('🐥', ''), ('🐦', '🐦'), ('🐧', '🐧'), ('🐸', '🐸'), ('🐢', ''), ('🐍', '🐍'), ('🐲', '🐲'), ('🐳', '🐳'), ('🐬', ''), ('🐟', '🐟'), ('🐠', ''), ('🐙', '🐙'), ('🐚', '🐚'), ('🐌', ''), ('🐛', ''), ('🐝', '🐝'), ('💐', ''), ('🌸', '🌸'), ('🌹', '🌹'), ('🌻', '🌻'), ('🌷', '🌷'), ('🌱', ''), ('🌴', ''), ('🌵', '🌵'), ('🌿', ''), ('🍀', ''), ('🍁', '🍁'), ('🍇', '🍇'), ('🍉', '🍉'), ('🍊', '🍊'), ('🍋', '🍋'), ('🍌', '🍌'), ('🍍', '🍍'), ('🍎', '🍎'), ('🍑', '🍑'), ('🍒', '🍒'), ('🍓', '🍓'), ('🍅', '🍅'), ('🍆', '🍆'), ('🌽', '🌽'), ('🍄', '🍄'), ('🍞', '🍞'), ('🍔', '🍔'), ('🍟', ''), ('🍕', '🍕'), ('🍙', ''), ('🍨', '🍨'), ('🍩', '🍩'), ('🍪', '🍪'), ('🍰', '🍰'), ('🍭', '🍭'), ('🍼', '🍼'), ('🍷', '🍷'), ('🍸', '🍸'), ('🍹', '🍹'), ('🍺', '🍺'), ('🍴', '🍴'), ('🌋', '🌋'), ('🏠', '🏠'), ('🏢', '🏢'), ('🏥', ''), ('🏩', '🏩'), ('🏰', ''), ('🌊', '🌊'), ('🎡', ''), ('🎢', ''), ('🎨', '🎨'), ('🚃', '🚃'), ('🚄', '🚄'), ('🚝', '🚝'), ('🚍', '🚍'), ('🚔', '🚔'), ('🚘', '🚘'), ('🚲', '🚲'), ('🚨', '🚨'), ('🚣', '🚣'), ('🚁', '🚁'), ('🚀', '🚀'), ('🚦', '🚦'), ('🚧', '🚧'), ('🚫', '🚫'), ('🚷', '🚷'), ('🚻', '🚻'), ('🚽', '🚽'), ('🚿', '🚿'), ('🛀', '🛀'), ('⏳', '⏳'), ('🌑', '🌑'), ('🌕', '🌕'), ('🌗', '🌗'), ('🌞', '🌞'), ('🌈', '🌈'), ('🌂', '🌂'), ('🌟', '🌟'), ('🔥', '🔥'), ('🎃', '🎃'), ('🎄', '🎄'), ('🎈', '🎈'), ('🎉', '🎉'), ('🎓', '🎓'), ('🎯', '🎯'), ('🎀', '🎀'), ('🏀', '🏀'), ('🏈', '🏈'), ('🎾', '🎾'), ('🎱', '🎱'), ('🏊', ''), ('🎮', '🎮'), ('🎲', '🎲'), ('📣', '📣'), ('📯', ''), ('🔔', '🔔'), ('🎶', '🎶'), ('🎤', '🎤'), ('🎹', '🎹'), ('🎺', '🎺'), ('🎻', '🎻'), ('📻', '📻'), ('📱', '📱'), ('📞', '📞'), ('🔋', '🔋'), ('🔌', '🔌'), ('💾', '💾'), ('💿', '💿'), ('🎬', '🎬'), ('📷', '📷'), ('🔍', '🔍'), ('🔭', '🔭'), ('💡', '💡'), ('📕', '📕'), ('📰', '📰'), ('💰', '💰'), ('💸', '💸'), ('📦', ''), ('📫', '📫'), ('💼', '💼'), ('📅', '📅'), ('📎', ''), ('📏', '📏'), ('📐', '📐'), ('🔑', '🔑'), ('🔩', '🔩'), ('💊', ''), ('🔪', '🔪'), ('🔫', '🔫'), ('🚬', '🚬'), ('🏁', ''), ('🔮', '🔮'), ('❌', '❌'), ('❓', '❓'), ('🔞', '🔞'), ('🆒', '🆒'), ('🆗', '🆗'), ('🆘', '🆘'), ('😙', '😙'), ('😑', '😑'), ('😮', '😮'), ('😴', '😴'), ('😛', '😛'), ('😧', '😧'), ('😬', '😬'), ('\U0001f575', '\U0001f575'), ('\U0001f595', '\U0001f595'), ('\U0001f596', '\U0001f596'), ('\U0001f441', '\U0001f441'), ('\U0001f576', '\U0001f576'), ('\U0001f6cd', '\U0001f6cd'), ('\U0001f43f', '\U0001f43f'), ('\U0001f54a', '\U0001f54a'), ('\U0001f577', '\U0001f577'), ('\U0001f336', '\U0001f336'), ('\U0001f3d5', ''), ('\U0001f3db', '\U0001f3db'), ('\U0001f6e2', '\U0001f6e2'), ('\U0001f6e5', ''), ('\U0001f6e9', ''), ('\U0001f6ce', '\U0001f6ce'), ('\U0001f570', '\U0001f570'), ('\U0001f321', '\U0001f321'), ('\U0001f324', '\U0001f324'), ('\U0001f327', '\U0001f327'), ('\U0001f329', '\U0001f329'), ('\U0001f32a', '\U0001f32a'), ('\U0001f32c', '\U0001f32c'), ('\U0001f396', '\U0001f396'), ('\U0001f397', '\U0001f397'), ('\U0001f39e', '\U0001f39e'), ('\U0001f3cb', ''), ('\U0001f3c5', '\U0001f3c5'), ('\U0001f579', '\U0001f579'), ('\U0001f399', '\U0001f399'), ('\U0001f5a5', '\U0001f5a5'), ('\U0001f5a8', '\U0001f5a8'), ('\U0001f5b2', '\U0001f5b2'), ('\U0001f4f8', ''), ('\U0001f56f', '\U0001f56f'), ('\U0001f5de', ''), ('\U0001f58b', '\U0001f58b'), ('\U0001f5d1', '\U0001f5d1'), ('\U0001f6e0', ''), ('\U0001f5e1', '\U0001f5e1'), ('\U0001f6e1', '\U0001f6e1'), ('\U0001f3f3', '\U0001f3f3'), ('\U0001f3f4', '\U0001f3f4'), ('\U0001f917', '\U0001f917'), ('\U0001f914', '\U0001f914'), ('\U0001f644', '\U0001f644'), ('\U0001f910', '\U0001f910'), ('\U0001f913', '\U0001f913'), ('\U0001f643', '\U0001f643'), ('\U0001f912', '\U0001f912'), ('\U0001f915', '\U0001f915'), ('\U0001f911', '\U0001f911'), ('\U0001f918', '\U0001f918'), ('\U0001f4ff', '\U0001f4ff'), ('\U0001f916', '\U0001f916'), ('\U0001f981', '\U0001f981'), ('\U0001f984', '\U0001f984'), ('\U0001f980', '\U0001f980'), ('\U0001f982', ''), ('\U0001f9c0', '\U0001f9c0'), ('\U0001f32d', '\U0001f32d'), ('\U0001f32e', '\U0001f32e'), ('\U0001f37f', '\U0001f37f'), ('\U0001f37e', '\U0001f37e'), ('\U0001f3cf', '\U0001f3cf'), ('\U0001f3d0', '\U0001f3d0'), ('\U0001f3d3', '\U0001f3d3'), ('\U0001f3f9', '\U0001f3f9'), ('\U0001f923', '\U0001f923'), ('\U0001f924', '\U0001f924'), ('\U0001f922', '\U0001f922'), ('\U0001f927', '\U0001f927'), ('\U0001f920', '\U0001f920'), ('\U0001f921', '\U0001f921'), ('\U0001f925', '\U0001f925'), ('\U0001f934', '\U0001f934'), ('\U0001f935', '\U0001f935'), ('\U0001f930', '\U0001f930'), ('\U0001f936', '\U0001f936'), ('\U0001f926', '\U0001f926'), ('\U0001f937', '\U0001f937'), ('\U0001f57a', '\U0001f57a'), ('\U0001f93a', '\U0001f93a'), ('\U0001f938', '\U0001f938'), ('\U0001f939', '\U0001f939'), ('\U0001f933', '\U0001f933'), ('\U0001f91e', '\U0001f91e'), ('\U0001f919', '\U0001f919'), ('\U0001f91b', '\U0001f91b'), ('\U0001f91c', '\U0001f91c'), ('\U0001f91a', '\U0001f91a'), ('\U0001f91d', '\U0001f91d'), ('\U0001f5a4', '\U0001f5a4'), ('\U0001f98a', '\U0001f98a'), ('\U0001f98c', '\U0001f98c'), ('\U0001f987', '\U0001f987'), ('\U0001f985', '\U0001f985'), ('\U0001f986', '\U0001f986'), ('\U0001f989', '\U0001f989'), ('\U0001f98e', '\U0001f98e'), ('\U0001f988', '\U0001f988'), ('\U0001f990', '\U0001f990'), ('\U0001f991', '\U0001f991'), ('\U0001f98b', '\U0001f98b'), ('\U0001f940', '\U0001f940'), ('\U0001f95d', '\U0001f95d'), ('\U0001f951', '\U0001f951'), ('\U0001f954', '\U0001f954'), ('\U0001f955', '\U0001f955'), ('\U0001f952', '\U0001f952'), ('\U0001f95c', '\U0001f95c'), ('\U0001f950', '\U0001f950'), ('\U0001f956', '\U0001f956'), ('\U0001f95e', '\U0001f95e'), ('\U0001f959', '\U0001f959'), ('\U0001f95a', '\U0001f95a'), ('\U0001f957', '\U0001f957'), ('\U0001f95b', '\U0001f95b'), ('\U0001f942', '\U0001f942'), ('\U0001f943', '\U0001f943'), ('\U0001f944', '\U0001f944'), ('\U0001f6f6', '\U0001f6f6'), ('\U0001f94a', '\U0001f94a'), ('\U0001f94b', '\U0001f94b'), ('\U0001f945', '\U0001f945'), ('\U0001f941', '\U0001f941'), ('\U0001f6d2', '\U0001f6d2')], default=None, max_length=2, null=True, verbose_name='emoji'),
        ),
        migrations.AlterField(
            model_name='team',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AlterField(
            model_name='team',
            name='long_name',
            field=models.CharField(editable=False, help_text='The full name of the team, including institution name. (This is autogenerated.)', max_length=200, verbose_name='long name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='reference',
            field=models.CharField(blank=True, help_text='Do not include institution name (see "uses institutional prefix" below)', max_length=150, verbose_name='full name/suffix'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.CharField(editable=False, help_text='The name shown in the draw, including institution name. (This is autogenerated.)', max_length=50, verbose_name='short name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_reference',
            field=models.CharField(blank=True, help_text='The name shown in the draw. Do not include institution name (see "uses institutional prefix" below)', max_length=35, verbose_name='short name/suffix'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterField(
            model_name='team',
            name='type',
            field=models.CharField(choices=[('N', 'None'), ('S', 'Swing'), ('C', 'Composite'), ('B', 'Bye')], default='N', max_length=1, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='team',
            name='url_key',
            field=models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='categories',
            field=models.ManyToManyField(blank=True, to='participants.SpeakerCategory', verbose_name='speaker categories'),
        ),
        migrations.AlterUniqueTogether(
            name='speakercategory',
            unique_together=set([('tournament', 'slug'), ('tournament', 'seq')]),
        ),
        migrations.AlterIndexTogether(
            name='speakercategory',
            index_together=set([('tournament', 'seq')]),
        ),
    ]
