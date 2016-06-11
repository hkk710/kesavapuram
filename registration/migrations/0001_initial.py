# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('aums_id', models.CharField(unique=True, max_length=32, verbose_name='Aums ID')),
                ('first_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='First Name', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('last_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Last Name', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email', db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
