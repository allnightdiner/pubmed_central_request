# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmc_request', '0006_auto_20150831_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMC_Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('author', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='pmcarticle',
            old_name='author_email',
            new_name='corresp_email',
        ),
        migrations.RemoveField(
            model_name='pmcarticle',
            name='author',
        ),
        migrations.AddField(
            model_name='pmc_article',
            name='pmc_article',
            field=models.ManyToManyField(to='pmc_request.PMCArticle'),
        ),
    ]
