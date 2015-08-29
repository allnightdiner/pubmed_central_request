# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0002_auto_20150828_2333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pmc_article',
            new_name='PMCArticle',
        ),
    ]
