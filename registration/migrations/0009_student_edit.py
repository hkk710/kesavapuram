# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20160130_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='edit',
            field=models.CharField(max_length=5, null=True, verbose_name='No of history arrears', blank=True),
        ),
    ]
