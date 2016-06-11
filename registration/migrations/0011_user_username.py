# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_remove_student_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 2, 14, 9, 39, 14, 382888, tzinfo=utc), unique=True, max_length=32, verbose_name='username'),
            preserve_default=False,
        ),
    ]
