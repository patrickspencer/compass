# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('max_problem_attempts', models.SmallIntegerField()),
                ('start_datetime', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('reduced_credit_due_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=40000)),
                ('seed', models.BigIntegerField()),
                ('start_datetime', models.DateTimeField()),
                ('grade', models.CharField(max_length=200)),
                ('attempts', models.PositiveIntegerField()),
                ('template_id', models.IntegerField()),
                ('assignments', models.ManyToManyField(to='assignments.Assignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
