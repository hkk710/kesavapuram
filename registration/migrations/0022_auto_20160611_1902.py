# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20160610_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='EligibilityTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantitativeTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReasoningTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerbalsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eligtest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='eligtest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='quanttest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='quanttest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='reasontest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='reasontest',
            name='test',
        ),
        migrations.RemoveField(
            model_name='verbtest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='verbtest',
            name='test',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Branch', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(null=True, verbose_name='CGPA', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.IntegerField(null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.IntegerField(null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s1',
            field=models.FloatField(null=True, verbose_name='S1 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s2',
            field=models.FloatField(null=True, verbose_name='S2 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s3',
            field=models.FloatField(null=True, verbose_name='S3 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s4',
            field=models.FloatField(null=True, verbose_name='S4 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s5',
            field=models.FloatField(null=True, verbose_name='S5 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s6',
            field=models.FloatField(null=True, verbose_name='S6 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.FloatField(null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.FloatField(null=True, verbose_name='12th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='aums_id',
            field=models.CharField(unique=True, max_length=32, verbose_name='Aums ID'),
        ),
        migrations.DeleteModel(
            name='EligTest',
        ),
        migrations.DeleteModel(
            name='QuantTest',
        ),
        migrations.DeleteModel(
            name='ReasonTest',
        ),
        migrations.DeleteModel(
            name='VerbTest',
        ),
        migrations.AddField(
            model_name='verbalstest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='verbalstest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='reasoningtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='reasoningtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='quantitativetest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='quantitativetest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='eligibilitytest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='eligibilitytest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
    ]
