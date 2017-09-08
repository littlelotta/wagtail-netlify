# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netlify_id', models.CharField(max_length=30, null=True)),
                ('url', models.URLField(null=True)),
                ('deployment_url', models.URLField(null=True)),
                ('datetime_started', models.DateTimeField(auto_now_add=True, help_text=b'deployment started')),
                ('datetime_finished', models.DateTimeField(null=True, verbose_name=b'deployment completed')),
            ],
        ),
    ]