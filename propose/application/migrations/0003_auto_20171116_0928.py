# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20171115_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workapplication',
            name='message',
        ),
        migrations.RemoveField(
            model_name='workoffer',
            name='is_expired',
        ),
        migrations.RemoveField(
            model_name='workrequest',
            name='message',
        ),
        migrations.AddField(
            model_name='applicationdetails',
            name='message',
            field=models.CharField(default=b'', max_length=2000),
        ),
        migrations.AddField(
            model_name='workoffer',
            name='application',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='application.WorkApplication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workoffer',
            name='expire_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workoffer',
            name='details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='application.ApplicationDetails'),
        ),
    ]