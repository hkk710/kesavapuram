# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0023_auto_20160616_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Your Name', blank=True)),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Your Star', blank=True)),
                ('manufacturer', models.CharField(max_length=100, null=True, verbose_name='Vazhipad Date', blank=True)),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, verbose_name='Price', validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
