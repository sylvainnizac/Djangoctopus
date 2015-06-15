# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='nbacces',
            field=models.SmallIntegerField(default=0),
        ),
    ]
