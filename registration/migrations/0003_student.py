# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_user_is_cir_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stud_id', models.AutoField(serialize=False, primary_key=True)),
                ('aums_id', models.CharField(unique=True, max_length=32, verbose_name='Aums ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='First Name', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('curr_course', models.CharField(blank=True, max_length=32, null=True, verbose_name='Current Course', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('branch', models.CharField(blank=True, max_length=32, null=True, verbose_name='Branch', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('tenth_mark', models.FloatField(null=True, verbose_name='10th Mark', blank=True)),
                ('twelth_mark', models.FloatField(null=True, verbose_name='12th Mark', blank=True)),
                ('s1', models.FloatField(null=True, verbose_name='S1 Mark', blank=True)),
                ('s2', models.FloatField(null=True, verbose_name='S2 Mark', blank=True)),
                ('s3', models.FloatField(null=True, verbose_name='S3 Mark', blank=True)),
                ('s4', models.FloatField(null=True, verbose_name='S4 Mark', blank=True)),
                ('s5', models.FloatField(null=True, verbose_name='S5 Mark', blank=True)),
                ('s6', models.FloatField(null=True, verbose_name='S6 Mark', blank=True)),
                ('cgpa', models.FloatField(null=True, verbose_name='S6 Mark', blank=True)),
                ('curr_arrears', models.FloatField(null=True, verbose_name='No of current arrears', blank=True)),
                ('hist_arrears', models.FloatField(null=True, verbose_name='No of history arrears', blank=True)),
            ],
        ),
    ]
