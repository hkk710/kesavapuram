# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20160610_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='aums_id',
            field=models.CharField(unique=True, max_length=32, verbose_name='Aums ID'),
        ),
    ]
