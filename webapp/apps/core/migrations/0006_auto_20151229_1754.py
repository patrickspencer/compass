# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_problemmapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemmapping',
            old_name='problem_id',
            new_name='problem',
        ),
        migrations.RenameField(
            model_name='problemmapping',
            old_name='user_id',
            new_name='user',
        ),
    ]
