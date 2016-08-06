# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_chocolate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aptitudetest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='aptitudetest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='eligibilitytest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='eligibilitytest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='hrtest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='hrtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='quantitativetest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='quantitativetest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='reasoningtest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='reasoningtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='techtest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='techtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='verbalstest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='verbalstest',
            name='test',
        ),
        migrations.DeleteModel(
            name='AptitudeTest',
        ),
        migrations.DeleteModel(
            name='EligibilityTest',
        ),
        migrations.DeleteModel(
            name='HRTest',
        ),
        migrations.DeleteModel(
            name='QuantitativeTest',
        ),
        migrations.DeleteModel(
            name='ReasoningTest',
        ),
        migrations.DeleteModel(
            name='TechTest',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='VerbalsTest',
        ),
    ]
