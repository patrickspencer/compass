# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 17:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_problem_seed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed', models.PositiveSmallIntegerField()),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Assignment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem_mappings',
            },
        ),
    ]
