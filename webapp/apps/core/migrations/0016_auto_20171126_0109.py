# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-26 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20171126_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='problem_mapping',
            new_name='problem_mapping_id',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='assignmentmapping',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='problemmapping',
            old_name='problem',
            new_name='problem_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='assignments',
            new_name='assignment',
        ),
    ]