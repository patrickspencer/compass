# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151227_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('seed', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'problems',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='assignments',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='string_id',
        ),
        migrations.AlterModelTable(
            name='assignment',
            table='assignments',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
