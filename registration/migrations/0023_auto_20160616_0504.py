# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20160611_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='student',
            name='curr_arrears',
        ),
        migrations.RemoveField(
            model_name='student',
            name='hist_arrears',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s3',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s4',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s5',
        ),
        migrations.RemoveField(
            model_name='student',
            name='s6',
        ),
        migrations.AlterField(
            model_name='student',
            name='aums_id',
            field=models.CharField(primary_key=True, serialize=False, choices=[(b'SreekrishnaSwamy', 'SreekrishnaSwamy'), (b'Ganapathi', 'Ganapathi'), (b'Devi', 'Devi'), (b'Nagar', 'Nagar')], max_length=32, unique=True, verbose_name='Prathishtta'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=32, null=True, verbose_name='Your Name', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_course',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')], choices=[(b'Ashttothara', 'Ashttothara'), (b'Vishnusahasranama', 'Vishnusahasranama'), (b'Bhagyasuktha', 'Bhagyasuktha'), (b'Swayawara', 'Swayawara')], max_length=32, blank=True, null=True, verbose_name='Vazhipad'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Vazhipad cattegory', choices=[(b'Archana', 'Archana'), (b'Homam', 'Homam'), (b'Pooja', 'Pooja'), (b'Samarppanam', 'Samarppanam')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.DateField(null=True, verbose_name='Vazhipad Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.FloatField(null=True, verbose_name='Price', blank=True),
        ),
    ]
