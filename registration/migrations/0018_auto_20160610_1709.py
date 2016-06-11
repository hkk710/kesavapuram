# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0017_auto_20160610_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='EligTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReasonTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerbTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='Mark', blank=True)),
            ],
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
            model_name='verbalstest',
            name='student',
        ),
        migrations.RemoveField(
            model_name='verbalstest',
            name='test',
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')], choices=[(b'CSE', 'CSE'), (b'ME', 'ME'), (b'EEE', 'EEE'), (b'EC', 'EC'), (b'CSA', 'CSA')], max_length=32, blank=True, null=True, verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.CharField(max_length=5, null=True, verbose_name='CGPA', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='curr_arrears',
            field=models.CharField(max_length=5, null=True, verbose_name='No of current arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist_arrears',
            field=models.CharField(max_length=5, null=True, verbose_name='No of history arrears', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s1',
            field=models.CharField(max_length=5, null=True, verbose_name='S1 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s2',
            field=models.CharField(max_length=5, null=True, verbose_name='S2 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s3',
            field=models.CharField(max_length=5, null=True, verbose_name='S3 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s4',
            field=models.CharField(max_length=5, null=True, verbose_name='S4 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s5',
            field=models.CharField(max_length=5, null=True, verbose_name='S5 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='s6',
            field=models.CharField(max_length=5, null=True, verbose_name='S6 Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.CharField(max_length=5, null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.CharField(max_length=5, null=True, verbose_name='12th Mark', blank=True),
        ),
        migrations.DeleteModel(
            name='EligibilityTest',
        ),
        migrations.DeleteModel(
            name='QuantitativeTest',
        ),
        migrations.DeleteModel(
            name='ReasoningTest',
        ),
        migrations.DeleteModel(
            name='VerbalsTest',
        ),
        migrations.AddField(
            model_name='verbtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='verbtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='reasontest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='reasontest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='quanttest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='quanttest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
        migrations.AddField(
            model_name='eligtest',
            name='student',
            field=models.ForeignKey(to='registration.Student'),
        ),
        migrations.AddField(
            model_name='eligtest',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
    ]
