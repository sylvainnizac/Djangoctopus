# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('shorturl', models.CharField(max_length=10)),
                ('longurl', models.URLField()),
                ('pseudo', models.CharField(null=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('nbacces', models.SmallIntegerField()),
            ],
        ),
    ]
