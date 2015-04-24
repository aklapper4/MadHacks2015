# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('R', models.IntegerField(default=0)),
                ('G', models.IntegerField(default=0)),
                ('B', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateTimeField(verbose_name=b'startDate')),
                ('endDate', models.DateTimeField(verbose_name=b'End')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(blank=True, to='taskmaster.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dueDate', models.DateTimeField(null=True, verbose_name=b'Due Date', blank=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('category', models.ForeignKey(blank=True, to='taskmaster.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.ForeignKey(to='taskmaster.Color'),
            preserve_default=True,
        ),
    ]
