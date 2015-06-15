# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0002_auto_20150613_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='pseudo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
