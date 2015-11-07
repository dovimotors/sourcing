# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcetrack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='int_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
