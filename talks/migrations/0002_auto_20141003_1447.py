# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('when', models.DateTimeField()),
                ('room', models.CharField(max_length=5, choices=[('517D', '517D'), ('517C', '517C'), ('517AB', '517AB')])),
                ('host', models.CharField(max_length=255)),
                ('talk_list', models.ForeignKey(related_name='talks', to='talks.TalkList')),
            ],
            options={
                'ordering': ('when', 'room'),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='talk',
            unique_together=set([('talk_list', 'name')]),
        ),
    ]
