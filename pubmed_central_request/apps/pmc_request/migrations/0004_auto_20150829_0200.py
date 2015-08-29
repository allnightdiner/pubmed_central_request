# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0003_auto_20150829_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='email_sent_timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
