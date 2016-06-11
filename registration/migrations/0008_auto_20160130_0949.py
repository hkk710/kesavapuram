# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20160130_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.CharField(max_length=5, null=True, verbose_name='CGPA', blank=True),
        ),
    ]
