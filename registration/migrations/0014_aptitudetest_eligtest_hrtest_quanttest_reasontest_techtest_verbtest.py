# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20160610_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='EligTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='HRTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='QuantTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='ReasonTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TechTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
        migrations.CreateModel(
            name='VerbTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
                ('test', models.ForeignKey(to='registration.Test')),
            ],
        ),
    ]
