# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('int_date', models.DateTimeField(verbose_name='date interviewed')),
                ('source', models.CharField(max_length=200)),
                ('employee', models.CharField(max_length=50)),
            ],
        ),
    ]
