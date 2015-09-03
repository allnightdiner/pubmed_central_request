# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0007_auto_20150903_1659'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PMC_Article',
            new_name='PMCAuthor',
        ),
    ]
