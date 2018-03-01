# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('telemeta', '0011_auto_20171215_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='roles',
            field=telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Roles', blank=True, choices=[(b'ENQ', b'Enqu\xc3\xaateur'), (b'INF', b'Informateur'), (b'AUT', b'Auteur'), (b'CMP', b'Compositeur'), (b'EDT', b'Editeur')]),
        )
    ]
