# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stud_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
    ]
