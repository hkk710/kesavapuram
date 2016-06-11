# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20160129_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.TextField(null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.TextField(null=True, verbose_name='12th Mark', blank=True),
        ),
    ]
