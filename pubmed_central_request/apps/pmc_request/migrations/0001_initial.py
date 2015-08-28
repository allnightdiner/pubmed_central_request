# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pmd_id', models.IntegerField()),
                ('accessed_url', models.URLField(max_length=2048)),
                ('request_timestamp', models.DateTimeField(auto_now=True)),
                ('article_accepted', models.BooleanField()),
                ('author_email', models.EmailField(max_length=254)),
                ('email_sent_timestamp', models.DateTimeField()),
            ],
        ),
    ]
