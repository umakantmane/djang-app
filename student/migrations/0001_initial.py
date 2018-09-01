# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_address', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
