# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20160129_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.TextField(null=True, verbose_name='S6 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.TextField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.TextField(null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s1',
            field=models.TextField(null=True, verbose_name='S1 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s2',
            field=models.TextField(null=True, verbose_name='S2 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s3',
            field=models.TextField(null=True, verbose_name='S3 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s4',
            field=models.TextField(null=True, verbose_name='S4 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s5',
            field=models.TextField(null=True, verbose_name='S5 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s6',
            field=models.TextField(null=True, verbose_name='S6 Mark', blank=True),
        ),
    ]
