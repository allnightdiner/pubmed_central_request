# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pmc_article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('pmc_id', models.IntegerField()),
                ('author_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='request',
            name='accessed_url',
        ),
        migrations.RemoveField(
            model_name='request',
            name='author_email',
        ),
        migrations.RemoveField(
            model_name='request',
            name='pmd_id',
        ),
        migrations.AddField(
            model_name='request',
            name='pmc_article',
            field=models.ForeignKey(to='pmc_request.pmc_article', default=0),
            preserve_default=False,
        ),
    ]
