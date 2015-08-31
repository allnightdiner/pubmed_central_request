# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0005_pmcarticle_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmcarticle',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pmcarticle',
            name='url',
            field=models.URLField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]
