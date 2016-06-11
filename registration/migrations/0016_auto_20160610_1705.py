# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20160610_1651'),
    ]

    operations = [
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
            model_name='user',
            name='aums_id',
            field=models.CharField(unique=True, max_length=32, verbose_name='Aums ID'),
        ),
    ]
