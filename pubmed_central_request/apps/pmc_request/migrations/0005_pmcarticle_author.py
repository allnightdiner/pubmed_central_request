# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0004_auto_20150829_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmcarticle',
            name='author',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
